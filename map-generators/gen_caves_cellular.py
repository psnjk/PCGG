import random
from PIL import Image, ImageDraw

# Powers of two please
MAP_SIZE = 2048
CELL_AMOUNT = 16

STEPS = 5



def create_grid(width, height):
    return [[0 for _x in range(width)] for _y in range(height)]


def initialize_grid(grid):
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for column in range(width):
            if random.random() <= 0.4:
                grid[row][column] = 1


def count_alive_neighbors(grid, x, y):
    height = len(grid)
    width = len(grid[0])
    alive_count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:
                continue
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_y >= height or neighbor_x >= width:
                # Edges are considered alive. Makes map more likely to appear naturally closed.
                alive_count += 1
            elif grid[neighbor_y][neighbor_x] == 1:
                alive_count += 1
    return alive_count


def do_simulation_step(old_grid):
    height = len(old_grid)
    width = len(old_grid[0])
    new_grid = create_grid(width, height)
    for x in range(width):
        for y in range(height):
            alive_neighbors = count_alive_neighbors(old_grid, x, y)
            if old_grid[y][x] == 1:
                if alive_neighbors < 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = 1
            else:
                if alive_neighbors > 4:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
    return new_grid

def create_image( grid):
    img = Image.new("RGB", (MAP_SIZE, MAP_SIZE), (78, 133, 121))
    offset = MAP_SIZE/CELL_AMOUNT
    draw = ImageDraw.Draw(img)

    for i in range(CELL_AMOUNT):
        for j in range(CELL_AMOUNT):
            if grid[i][j] == 0:
                draw.rectangle(((j*offset, i*offset), (offset+j*offset, offset+i*offset)), (117, 199, 181))
    return img

grid = create_grid(CELL_AMOUNT, CELL_AMOUNT)
initialize_grid(grid)
for step in range(4):
    grid = do_simulation_step(grid)
    #create_image(grid).save('celmap'+ str(CELL_AMOUNT)+ '_' + str(MAP_SIZE)+ '_' + str(step)+'.png')

create_image(grid).save('celmap'+ str(CELL_AMOUNT)+ '_' + str(MAP_SIZE)+ '_' + str(STEPS)+'.png')


import numpy as np
from PIL import Image, ImageDraw
import random

rooms = []


def check_coll(x, y, size_x, size_y):
    flag = True
    
    for room in rooms:
        if (
            (x >= room.x1 and y >= room.y1 and x <= room.x2 and y <= room.y2) or
            (x + size_x - 1 >= room.x1 and y >= room.y1 and x + size_x - 1 <= room.x2 and y <= room.y2) or
            (x >= room.x1 and y + size_y - 1 >= room.y1 and x <= room.x2 and y + size_y - 1 <= room.y2) or
            (x + size_x - 1 >= room.x1 and y + size_y - 1 >= room.y1 and x + size_x - 1 <= room.x2 and y + size_y - 1 <= room.y2)
        ):
            #print('Collision with ' + room.name)
            flag = False
        else:
            pass
            #print('No collision!')

    if (x < 0 or y < 0 or x > 63 or y > 63):
        print('Out of map')
        flag = False

    return flag


# [0, 3] - corridor
# 4 - intersection
# 5 - room
# 6 - deadend
def what_is_next():
    nxt = random.randint(0, 6)
    if nxt < 4:
        return 0
    elif nxt == 4:
        return 1
    elif nxt == 5:
        return 2
    elif nxt == 6:
        return 3
    else:
        print('Nonsense!')


class room:
    size_x = 0
    size_y = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    name = 'unsigned'
    color = (0, 0, 0)

    def __init__(self, x, y, size_x, size_y, name, color):
        self.size_x = size_x
        self.size_y = size_y
        self.x1 = x
        self.y1 = y
        self.x2 = self.x1 + self.size_x - 1
        self.y2 = self.y1 + self.size_y - 1
        self.name = name
        self.color = color

    def gen_ways(self, direction):
        gen_map(gen_background()).save('map.png')
        ######################################################################
        if self.name == 'Ladder':
            print('put room ' + self.name + ' at ' + str(self.x1) + ' ' + str(self.y1))
            ways = [1, 2, 3, 4]
            random.shuffle(ways)
            for dir in ways:
                if dir == 1:
                    print('Up from ladder')
                    x = self.x1 + self.size_x//2
                    y = self.y1 - 1
                elif dir == 2:
                    print('Left from ladder')
                    x = self.x1 - 1
                    y = self.y1 + self.size_y//2
                elif dir == 3:
                    print('Right from ladder')
                    x = self.x1 + self.size_x
                    y = self.y1 + self.size_y//2
                elif dir == 4:
                    print('Down from ladder')
                    x = self.x1 + self.size_x//2
                    y = self.y1 + self.size_y
                else:
                    print('Not possible')
                if check_coll(x, y, 1, 1):
                    nxt = what_is_next()
                    if nxt == 0:
                        to_add = room(x, y, 1, 1, 'Corridor', (100, 100, 100))
                        rooms.append(to_add)
                        to_add.gen_ways(dir)
                    if nxt == 1:
                        to_add = room(x, y, 1, 1, 'Intersection', (150, 150, 150))
                        rooms.append(to_add)
                        to_add.gen_ways(dir)
                    if nxt == 2:
                        to_add = room(x, y, 1, 1, 'Deadend', (50, 50, 50))
                        rooms.append(to_add)
                    if nxt == 2:
                        to_add = room(x, y, 1, 1, 'Deadend', (50, 50, 50))
                        rooms.append(to_add)
        ######################################################################
        elif self.name == 'Corridor':
            print('put room ' + self.name + ' at ' + str(self.x1) + ' ' + str(self.y1))
            if direction == 1:
                print('Corridor up')
                x = self.x1 + self.size_x//2
                y = self.y1 - 1
            elif direction == 2:
                print('Corridor left')
                x = self.x1 - 1
                y = self.y1 + self.size_y//2
            elif direction == 3:
                print('Corridor right')
                x = self.x1 + self.size_x
                y = self.y1 + self.size_y//2
            elif direction == 4:
                print('Corridor down')
                x = self.x1 + self.size_x//2
                y = self.y1 + self.size_y
            else:
                print('wtf')

            if check_coll(x, y, 1, 1):
                nxt = what_is_next()
                if nxt == 0:
                    to_add = room(x, y, 1, 1, 'Corridor', (100, 100, 100))
                    rooms.append(to_add)
                    to_add.gen_ways(direction)
                if nxt == 1:
                    to_add = room(x, y, 1, 1, 'Intersection', (150, 150, 150))
                    rooms.append(to_add)
                    to_add.gen_ways(direction)
                if nxt == 2:
                    to_add = room(x, y, 1, 1, 'Deadend', (50, 50, 50))
                    rooms.append(to_add)
                if nxt == 2:
                    to_add = room(x, y, 1, 1, 'Deadend', (50, 50, 50))
                    rooms.append(to_add)
        ######################################################################
        elif self.name == 'Intersection':
            print('put room ' + self.name + ' at ' + str(self.x1) + ' ' + str(self.y1))
            ways = [1, 2, 3, 4]
            random.shuffle(ways)
            move = False
            for dir in ways:
                if dir == 1 and direction!=4:
                    print('Up from intersection')
                    x = self.x1 + self.size_x//2
                    y = self.y1 - 1
                    move = True
                elif dir == 2 and direction!=3:
                    print('Left from intersection')
                    x = self.x1 - 1
                    y = self.y1 + self.size_y//2
                    move = True
                elif dir == 3 and direction!=2:
                    print('Right from intersection')
                    x = self.x1 + self.size_x
                    y = self.y1 + self.size_y//2
                    move = True
                elif dir == 4 and direction!=1:
                    print('Down from intersection')
                    x = self.x1 + self.size_x//2
                    y = self.y1 + self.size_y
                    move = True
                else:
                    print('Not possible')
                if move:
                    if check_coll(x, y, 1, 1):
                        nxt = what_is_next()
                        if nxt == 0:
                            to_add = room(x, y, 1, 1, 'Corridor', (100, 100, 100))
                            rooms.append(to_add)
                            to_add.gen_ways(dir)
                        if nxt == 1:
                            to_add = room(x, y, 1, 1, 'Intersection', (150, 150, 150))
                            rooms.append(to_add)
                            to_add.gen_ways(dir)
                        if nxt == 2:
                            to_add = room(x, y, 1, 1, 'Deadend', (50, 50, 50))
                            rooms.append(to_add)
                        if nxt == 2:
                            to_add = room(x, y, 1, 1, 'Deadend', (50, 50, 50))
                            rooms.append(to_add)
        ######################################################################


def gen_background():

    img = Image.new("RGB", (512, 512), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(64):
        for j in range(64):
            draw.rectangle(((j*8, i*8), (8+j*8, 8+i*8)), (0, 0, 0), outline=(20, 20, 20))

    return img


def gen_start1():
    x = random.randint(16, 48)
    y = random.randint(16, 48)
    return room(x, y, 3, 3, 'Ladder', (3, 252, 240))


def gen_start(x, y):
    return room(x, y, 3, 3, 'Ladder', (3, 252, 240))


def gen_corridor(x, y, amo):
    for i in range(amo):
        rooms.append()

def gen_map(img):
    draw = ImageDraw.Draw(img)
    for i in rooms:
        draw.rectangle(((i.x1*8, i.y1*8), (8+i.x2*8, 8+i.y2*8)), i.color)
    return img

back = gen_background()
start = gen_start1()
rooms.append(start)



start.gen_ways(0)



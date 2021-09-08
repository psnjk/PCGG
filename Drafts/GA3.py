
from PIL import Image, ImageDraw, ImageFont, ImageChops
import time
import random
import numpy as np
import copy

src = Image.open('anime.jpg')

def get_difference(image,image_src):
    difference = ImageChops.difference(image, image_src)
    histogram = difference.histogram()
    squares = (value * ((index % 256) ** 2) for index, value in enumerate(histogram))
    sum_of_squares = np.sum(squares)
    rms = sum_of_squares / float(image.size[0] * image.size[1])
    return rms

def get_fitness(image):
    return get_difference(image, src)

def gen_image():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    img = Image.new("RGB", (512,512), (r,g,b))
    draw = ImageDraw.Draw(img)
    for i in range(64):
        
        for j in range(64):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            draw.line([(j*8,i*8),(8 + j*8,8 + i*8)],(r,g,b),2)
    return img

def get_population(size):
    pop = []
    for i in range(size):
        pop.append([gen_image(),1000000])
    return pop

def get_best(pop, size):
    best_fit = 10000000
    
    for i in range(size):
        pop[i][1] = get_fitness(pop[i][0])
        if best_fit > pop[i][1]:
            best_fit = pop[i][1]
    
    for i in range(size//2):
        max = 0
        for j in range(size-i):
            if pop[max][1] < pop[j][1]:
                max = j
        pop.pop(max)
        max = 0

    
    return [pop,best_fit]


def crossover(population, size):
    new_generation = []
    for i in range(size//2):

        pair = i + 1
        if i+1 == size//2:
            pair = 0

        new_individual = Image.blend(population[i][0], population[pair][0], 0.5)
        new_generation.append([new_individual,1000000])

    return new_generation

def mutation(individual):
    draw = ImageDraw.Draw(individual[0])
    place1 = random.randint(0,63)
    place2 = random.randint(0,63)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    draw.line([(place1*8,place2*8),(8 + place1*8,8 + place2*8)],(r,g,b),2)
    return individual


def start_genetic():
    fit = 100000
    prevfit = 50000
    iteration = 1
    pop = get_population(10)

    while (fit>2000):
        best = get_best(pop,10)
        pop = best[0]
        fit = best[1]
        pop.extend(crossover(pop,10))
        #to_mutate = random.randint(5,9)
        #pop[to_mutate] = mutation(pop[to_mutate])
        pop[5] = mutation(pop[5])
        pop[6] = mutation(pop[6])
        pop[7] = mutation(pop[7])
        pop[8] = mutation(pop[8])
        if (prevfit > fit + 50):
            prevfit = fit
        #if(iteration%50 == 0) or (iteration==1):
            print("Iteration ",iteration,", best fitness = ", fit)
            pop[0][0].save("./test/test" + str(fit) + ".png")
        iteration += 1

    for i in range(10):
        pop[i][0].save("./test/test" + str(i) + ".png")
    

#get_image(img).save("result.png")
start_genetic()

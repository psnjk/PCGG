import random
import math

random.seed(0)

def generateWhiteNoise(width,height):
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(0,height):
        for j in range(0,width):
            noise[i][j] = random.randint(0,1)

    return noise

noise = generateWhiteNoise(50,12)

for i in noise:
    print()
    for o in i:
        if(o == 0):
            print('-',end='')
        else:
            print('#',end='')
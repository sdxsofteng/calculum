import sys
import math

# game loop
while True:
    max = -1
    index = -1
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > max:
            index = i
            max = mountain_h
    print(index)
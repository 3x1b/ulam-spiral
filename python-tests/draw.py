import pygame
import math
import asyncio

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

positions = []
position = (0, 0)

dirs = [
    (1, 0),
    (0, -1),
    (-1, 0),
    (0, 1)
]

def soePrimeGenerator(amnt):
    global running

    primes = [True for _ in range(amnt + 1)]
    cur = 2
    while (cur * cur <= amnt):
        if primes[cur] == True:
            for i in range(cur * cur, amnt+1, cur):
                primes[i] = False
        cur += 1
    
    return primes

x, y = 0, 0
points = []
    
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
size = 1
dr = 0 
idx = 1
width = 100

primes = soePrimeGenerator(((2 * width) + 1) ** 2)

while size <= width:
    for _ in range(size):
        x += directions[dr][0]
        y += directions[dr][1]
        idx += 1
        if primes[idx]:
            points.append((x + (width // 2), y + (width // 2)))

    size += dr & 1
        
    dr = (dr + 1) & 3

update = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    size = (720 / (1 + width))

    if update:
        for y in range(1 + width):
            for x in range(1 + width):
                if (x, y) in points:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((size * x) - 0.5, (size * ((1 + width) - y)) - 0.5, size + 1, size + 1))

        pygame.display.flip()
        update = False

    clock.tick(60)

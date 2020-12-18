#!/usr/bin/python3

import pygame

import calc_impr as calc

import time

WIDTH = 500
HEIGHT = 500

def main() -> int:
    pygame.init()
    calc.init()

    calc.set_colors((156,  38, 177),
                    ( 64,  82, 182),
                    (  0, 169, 246))

    FPS = 30
    screen = pygame.display.set_mode((2*WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    finished = False

    zero = time.time()

    points = calc.calc(WIDTH, HEIGHT, 0, 0, 3, 3, -0.1225611669, -0.7448617670, 0, 0, 3, 3)

    first = time.time()
    newSurf_m = pygame.surfarray.make_surface(points[0])
    screen.blit(newSurf_m, (0, 0))

    newSurf_j = pygame.surfarray.make_surface(points[1])
    screen.blit(newSurf_j, (WIDTH, 0))

    second = time.time()

    calc.free()

    pygame.display.update()

    print("Calc:", first - zero)
    print("Render:", second - first)

    while (not finished):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()
    return 0

if (__name__ == "__main__"):
    main()

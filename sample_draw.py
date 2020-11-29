#!/usr/bin/python3

import pygame

import calc_simple as calc

import time

def main() -> int:
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((2*calc.WIDTH, calc.HEIGHT))

    clock = pygame.time.Clock()
    finished = False

    zero = time.time()

    points = calc.calc(0, 0, 3, 3, -0.1225611669, -0.7448617670, 0, 0, 3, 3)

    first = time.time()
    newSurf_m = pygame.surfarray.make_surface(points[0])
    screen.blit(newSurf_m, (0, 0))

    newSurf_j = pygame.surfarray.make_surface(points[1])
    screen.blit(newSurf_j, (calc.WIDTH, 0))

    second = time.time()

    pygame.display.update()

    while (not finished):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

    print("Calc:", first - zero)
    print("Render:", second - first)
    return 0

if (__name__ == "__main__"):
    main()

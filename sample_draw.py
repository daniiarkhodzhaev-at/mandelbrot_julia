#!/usr/bin/python3

import pygame

import calc_simple as calc

def main() -> int:
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((2*calc.WIDTH, calc.HEIGHT))

    clock = pygame.time.Clock()
    finished = False

    points = calc.calc(0, 0, 3, 3, -0.1225611669, -0.7448617670, 0, 0, 3, 3)
    surface_m = pygame.Surface((calc.WIDTH, calc.HEIGHT))
    pixelArray_m = pygame.PixelArray(surface_m)
    for x in range(calc.WIDTH):
        for y in range(calc.HEIGHT):
            pixelArray_m[x, y] = points[0][x][y]
    newSurf_m = pixelArray_m.make_surface()
    screen.blit(newSurf_m, (0, 0))

    surface_j = pygame.Surface((calc.WIDTH, calc.HEIGHT))
    pixelArray_j = pygame.PixelArray(surface_j)
    for x in range(calc.WIDTH):
        for y in range(calc.HEIGHT):
            pixelArray_j[x, y] = points[1][x][y]
    newSurf_j = pixelArray_j.make_surface()
    screen.blit(newSurf_j, (calc.WIDTH, 0))

    pygame.display.update()

    while (not finished):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()
    return 0

if (__name__ == "__main__"):
    main()

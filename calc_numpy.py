#!/usr/bin/python3

import numpy as np

NUM_STEPS = 1024;

WIDTH = 800
HEIGHT = 800

def __scale(color: tuple, a: float) -> tuple:
    assert len(color) == 3
    return (color[0] * a, color[1] * a, color[2] * a)

# tmp solution
COLORS = (__scale((0.61, 0.15, 0.69), 255),
          __scale((0.25, 0.32, 0.71), 255),
          __scale((0.00, 0.66, 0.96), 255))

def __color_sum(color1: tuple, color2: tuple) -> tuple:
    assert len(color1) == 3
    assert len(color2) == 3
    return (color1[0] + color2[0], color1[1] + color2[1], color1[2] + color2[2])

def _get_color(n: int, colors: tuple) -> tuple:
    if (n == NUM_STEPS):
        return (0.0 ,0.0 ,0.0)
    
    i = n % 20 / 20
    cel = n // 20 % 3

    color1 = colors[0]
    color2 = colors[1]
    color3 = colors[2]

    if (cel == 0):
        return __color_sum(__scale(color1, i), __scale(color2, (1 - i)))

    if (cel == 1):
        return __color_sum(__scale(color3, i), __scale(color1, (1 - i)))

    if (cel == 2):
        return __color_sum(__scale(color2, i), __scale(color3, (1 - i)))

    return (0.0, 0.0, 0.0)

# TODO: add color array
def calc(mx: float, my: float, dmx: float, dmy: float,
        cx: float, cy: float,
        jx: float, jy: float, djx: float, djy: float) -> tuple:
    """
    This is the main function of module. It calculates the colors of pixels
    for requested areas of Mandelbrot and Julia sets.

    @param mx --- real part of center of requested area of Mandelbrot set
    @param my --- imaginary part of center of requested area of Mandelbrot set
    @param dmx --- width (size along real axis) of requested area of Mandelbrot set
    @param dmy --- height (size along imaginary axis) of requested area of Mandelbrot set

    @param cx --- real coord of requested c-point for Julia set
    @param cy --- imaginary coord of requested c-point for Julia set

    @param jx --- real part of center of requested area of Julia set
    @param jy --- imaginary part of center of requested area of Julia set
    @param djx --- width (size along real axis) of requested area of Julia set
    @param djy --- height (size along imaginary axis) of requested area of Julia set

    @return typle --- 2d list of pixel colors (color --- rgb tuple)
    """
    m_points_r = np.full((WIDTH, HEIGHT), 0.0)
    m_points_g = np.full((WIDTH, HEIGHT), 0.0)
    m_points_b = np.full((WIDTH, HEIGHT), 0.0)
    m_filled = np.full((WIDTH, HEIGHT), 0)
    m_x0 = np.full((WIDTH, HEIGHT), 0.0)
    m_y0 = np.full((WIDTH, HEIGHT), 0.0)
    mcx, mcy = np.meshgrid(np.linspace(mx - dmx / 2, mx + dmx / 2, WIDTH), np.linspace(my - dmy / 2, my + dmy / 2, HEIGHT), indexing="ij")
    for it in range(NUM_STEPS+1):
        m_x0, m_y0 = m_x0 ** 2 - m_y0 ** 2 + mcx, 2 * m_x0 * m_y0 + mcy
        m_div = m_x0 ** 2 + m_y0 ** 2 > 4.0
        m_div = m_div.astype(np.int)
        m_div -= m_div * m_filled
        m_color = _get_color(it, COLORS)
        m_points_r += m_div * m_color[0]
        m_points_g += m_div * m_color[1]
        m_points_b += m_div * m_color[2]
        m_filled += m_div
    m_points = np.dstack((m_points_r, m_points_g, m_points_b))

    j_points_r = np.full((WIDTH, HEIGHT), 0.0)
    j_points_g = np.full((WIDTH, HEIGHT), 0.0)
    j_points_b = np.full((WIDTH, HEIGHT), 0.0)
    j_filled = np.full((WIDTH, HEIGHT), 0)
    j_x0, j_y0 = np.meshgrid(np.linspace(jx - djx / 2, jx + djx / 2, WIDTH), np.linspace(jy - djy / 2, jy + djy / 2, HEIGHT), indexing="ij")
    for it in range(NUM_STEPS+1):
        j_x0, j_y0 = j_x0 ** 2 - j_y0 ** 2 + cx, 2 * j_x0 * j_y0 + cy
        j_div = j_x0 ** 2 + j_y0 ** 2 > 4.0
        j_div = j_div.astype(np.int)
        j_div -= j_div * j_filled
        j_color = _get_color(it, COLORS)
        j_points_r += j_div * j_color[0]
        j_points_g += j_div * j_color[1]
        j_points_b += j_div * j_color[2]
        j_filled += j_div
    j_points = np.dstack((j_points_r, j_points_g, j_points_b))

    return (m_points, j_points)

if (__name__ == "__main__"):
    print("TODO: write test script")

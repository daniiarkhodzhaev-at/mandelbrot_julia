#!/usr/bin/python3

NUM_STEPS = 1024;

WIDTH = 400
HEIGHT = 400

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

def _julia_number_of_term(x: float, y: float, cx: float, cy: float) -> int:
    x0, y0 = x, y
    i = 0
    while (x0 * x0 + y0 * y0 <= 4 and i < NUM_STEPS):
        x0, y0 = x0 * x0 - y0 * y0 + cx, 2 * x0 * y0 + cy
        i += 1

    return i

def _mandelbrot_number_of_term(x: float, y: float) -> int:
    return _julia_number_of_term(0, 0, x, y)

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
    m_points = [[(0, 0, 0) for _ in range(HEIGHT)] for _ in range(WIDTH)]
    for i in range(WIDTH):
        for j in range(HEIGHT):
            m_points[i][j] = _get_color(_mandelbrot_number_of_term(
                mx - dmx / 2 + dmx * i / HEIGHT, my - dmy / 2 + dmy * j / HEIGHT), COLORS)
    j_points = [[(0, 0, 0) for _ in range(HEIGHT)] for _ in range(WIDTH)]
    for i in range(WIDTH):
        for j in range(HEIGHT):
            j_points[i][j] = _get_color(_julia_number_of_term(
                jx - djx / 2 + djx * i / HEIGHT, jy - djy / 2 + djy * j / HEIGHT, cx, cy), COLORS)
    return (m_points, j_points)

if (__name__ == "__main__"):
    print("TODO: write test script")

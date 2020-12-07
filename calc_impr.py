#!/usr/bin/python3

import numpy as np
import ctypes

def init() -> None:
    global ccalc, buff
    ccalc = ctypes.cdll.LoadLibrary("calc.so")
    ccalc._calc_man.restype = ctypes.c_void_p;
    ccalc._calc_man.argtypes = [ctypes.c_int, ctypes.c_int,\
            ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]

    ccalc._calc_jul.restype = ctypes.c_void_p;
    ccalc._calc_jul.argtypes = [ctypes.c_int, ctypes.c_int,\
            ctypes.c_double, ctypes.c_double,\
            ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]

    buff = []

    return


# TODO: add color array
def calc(width: int, height: int,
        mx: float, my: float, dmx: float, dmy: float,
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
    global buff
    
    m_pointer = ccalc._calc_man(width, height, mx, my, dmx, dmy)
    m_pointer = ctypes.cast(m_pointer, ctypes.POINTER(ctypes.c_int))
    m_points = np.ctypeslib.as_array(m_pointer, shape=(width, height, 3))
    buff.append(m_pointer)

    j_pointer = ccalc._calc_jul(width, height, cx, cy, jx, jy, djx, djy)
    j_pointer = ctypes.cast(j_pointer, ctypes.POINTER(ctypes.c_int))
    j_points = np.ctypeslib.as_array(j_pointer, shape=(width, height, 3))
    buff.append(j_pointer)

    return (m_points, j_points)

def free() -> None:
    global buff
    for p in buff:
        ccalc._free(p)
    buff = []
    return

if (__name__ == "__main__"):
    print("TODO: write test script")

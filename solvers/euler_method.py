# Euler method with fixed step

import numpy as np


def euler_method(fx, x0, consts, ti, tf, steps):

    m = len(x0)
    h = (tf-ti)/steps
    T = []
    R = []
    # initial conditions 
    T.append(ti)
    R.append(x0)
    # the euler steps
    for j in range(int(steps)):

        R.append(np.multiply(h, fx(T[j], R[j], consts[:])) + R[j])
        T.append(ti+j*h)

    return [T, R]



# Euler method with fixed step

import numpy as np

def euler_method(fx,x0,consts,ti,tf,steps):
    m = len(x0)
    h = (tf-ti)/steps
    T = []
    R = []
    # initial conditions 
    T.append(ti)
    R.append(x0)
    # the euler steps
    for j in range(0,int(tf)):

        R.append(fx(T[j], np.multiply(h, R[j]) + R[j], consts[:]))
        T.append(ti+j*h)

    return [T, R]



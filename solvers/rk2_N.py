import numpy as np

def rk2_N(fx, x0, consts, ti, tf, steps):
    n = len(x0)
    w = []
    w.append(x0)
    t = []
    t.append(ti)
    k1 = []
    k2 = []
    h = 1.0 * (tf - ti) / steps
    for i in range(0, steps):
        k1 = np.multiply(h, fx(t[i], w[i], consts[:]))
        k2 = np.multiply(h, fx(t[i] + h , w[i] + 1 * k1, consts[:]))
        w.append(w[i] + (k1 + 1 * k2 ) / 2)
        t.append(ti + i * h)

    return [t, w]

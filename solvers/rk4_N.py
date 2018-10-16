#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:57:15 2018

@author: jl
"""
import numpy as np


def rk4_1(fx, x0, ti, tf, steps):
    """
    4th order Runge-Kutta method
    :param fx: function to be iterated
    :param x0: initial conditions of in list for of size n, data type float
    :param ti: initial time (int)
    :param tf: final time (int)
    :param steps: number of steps required (int)
    :return: a 2-D list with the time in list form, and the solution for every iteration time
    """
    n = len(x0)
    w, t = [], []
    w.append(x0)
    t.append(ti)

    h = 1.0*(tf-ti)/steps
    for i in range (0, steps):

        k1 = np.multiply(h, fx(t[i], w[i]))
        k2 = np.multiply(h, fx(t[i]+h/2, w[i]+0.5*k1))
        k3 = np.multiply(h, fx(t[i]+h/2, w[i]+0.5*k2))
        k4 = np.multiply(h, fx(t[i]+h, w[i]+k3))
         
        w.append(w[i]+(k1+2*k2+2*k3+k4)/6)
        t.append(ti+i*h)
    
    return [t, w]


#  This one admits constants if you need to change them
def rk4_N(fx, x0, consts, ti, tf, steps):
    """
    4th order Runge-Kutta method with the option to pass the constant of the function separately, useful when you need
    to solve a system for different values of its parameters.
    :param fx: function to be iterated
    :param x0: initial conditions of in list for of size n, data type float
    :param consts: the parameters of your ODE system
    :param ti: initial time (int)
    :param tf: final time (int)
    :param steps: number of steps required (int)
    :return: a 2-D list with the time in list form, and the solution for every iteration time
    """

    w, t = [], []
    w.append(x0)
    t.append(ti)

    h = 1.0 * (tf-ti)/steps

    for i in range(steps):

        k1 = np.multiply(h, fx(t[i], w[i], consts[:]))
        k2 = np.multiply(h, fx(t[i] + h/2, w[i] + 0.5*k1, consts[:]))
        k3 = np.multiply(h, fx(t[i] + h/2, w[i] + 0.5*k2, consts[:]))
        k4 = np.multiply(h, fx(t[i] + h, w[i]+k3, consts[:]))
         
        w.append(w[i] + (k1 + 2*k2 + 2*k3 + k4)/6)
        t.append(ti + i*h)

    return [t, w]

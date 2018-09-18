#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:57:15 2018

@author: jl
"""
import numpy as np


def rk4_1(fx, x0, ti, tf, steps):
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


def rk4_N(fx,x0,consts,ti,tf,steps):
    n = len(x0)
    w, t = [], []
    w.append(x0)
    t.append(ti)
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    h = 1.0*(tf-ti)/steps
    for i in range (0,steps):
        k1 = np.multiply(h, fx(t[i], w[i], consts[:]))
        k2 = np.multiply(h, fx(t[i]+h/2, w[i]+0.5*k1, consts[:]))
        k3 = np.multiply(h, fx(t[i]+h/2, w[i]+0.5*k2, consts[:]))
        k4 = np.multiply(h, fx(t[i]+h, w[i]+k3, consts[:]))
         
        w.append(w[i]+(k1+2*k2+2*k3+k4)/6)
        t.append(ti+i*h)


    return [t, w]

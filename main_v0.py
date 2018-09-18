#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: jl
"""
import numpy as np
from solvers.rk4_N import*
from solvers.euler_method import*
from models.SI_model import SI_model
from models.SIR_model import SIR_model
import matplotlib.pyplot as plt


x01 = 500
x02 = 200
x03= 1
x0 = [x01, x02, x03]
consts = [0.1, 0.2, 0.3]

y = rk4_N(SIR_model, x0, consts, 0, 50, 1000)
y1,y2, y3=[],[],[]
for ye in y[1]:

    y1.append(ye[0])
    y2.append(ye[1])
    y3.append(ye[2])

plt.figure(1)
plt.plot(y[0], y1,'--')
plt.plot(y[0], y2,'--')
plt.plot(y[0], y3,'--')

plt.show()

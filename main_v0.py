#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: jl
"""
import numpy as np
from solvers.rk4_N import*
import matplotlib.pyplot as plt
from exact_solutions import*
from solvers.rk2_N import rk2_N
from solvers.euler_method import*
from models.SI_model import SI_model
from models.SIR_model import SIR_model
from models.SI_model2 import SI_model2


N=1
x01 = 1/N
x02 = 0.01/N
x03= 0/N
x0 = [x01, x02, x03] # change this according to the entries of your model

c_1 = 1.4
c_2 = 0.09
c_3 = 0.1
consts = [c_1, c_2] # change this according to the number of constants  of your model

initial_time = 0 
final_time = 50
total_number_of_steps = 500
y = rk4_N(SIR_model, x0, consts, initial_time, final_time, total_number_of_steps)

sir = SIR_sol(x01, x02, x03, c_1, c_2, final_time)
sis = SIS_sol(x01, x02, c_1, c_2, final_time)
y1,y2, y3=[],[],[]
for ye in y[1]:

    y1.append(ye[0])
    y2.append(ye[1])
    y3.append(ye[2])

plt.figure(1)
plt.plot(y[0], y1, '-o')
plt.plot(y[0], y2, '-o')
plt.plot(y[0], y3, '-o')

plt.figure(2)
plt.plot(sir[0], 'b')
plt.plot(sir[1], 'r')

plt.figure(3)
plt.plot(sis[0], 'b')
plt.plot(sis[1], 'r')
plt.show()

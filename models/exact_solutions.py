#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: jl
"""
# This program has 2 functions which calculate the solutions of the SIR and SIS
# model presented in Shabbir et al. A note on Exact solution of SIR and SIS epidemic models
# https://arxiv.org/pdf/1012.5035.pdf
import numpy as np
import copy


def SIR_sol(s_0, i_0, r_0, beta, mu, total_time, steps):

    """
    :param s_0: Initial population of susceptible
    :param i_0: Initial population of infected
    :param r_0: Initial population of recovered
    :param beta: const
    :param mu: const
    :return: Susceptibles through time, Infected through time
    """

    S = []
    I = []
    R = []

    #S.append(s_0)
    #I.append(i_0)
    #R.append(r_0)

    C = s_0 + i_0 - 1
    lambd = beta - mu + beta * C
    D = (lambd - i_0 * beta) / (lambd * i_0 * np.exp(beta * C / mu))

    for j in range(0, total_time):

        t = j*0.4

        param = beta + lambd * D * np.exp(- lambd * t) * np.exp(beta * C / mu)
        S.append((1 + (s_0 + i_0 - 1) * (1 - mu * t) - lambd/(beta + lambd * D * np.exp(- lambd * t + (beta * C) / mu))))
        I.append(lambd/(beta + lambd * D * np.exp(-lambd * t) * np.exp((beta * C) / mu)))
        R.append(r_0 + mu * I[j] * t)
    
    return [S, I, R]



def SIR2_sol(s_0, i_0, r_0, beta, gamma, total_time, steps):

    def f(x, c, gamma, beta, s_0):
        fx = 1 / (x * (c-gamma * np.log(x) + s_0 * beta * x))
        return fx

    """
    :param s_0: Initial population of susceptibles
    :param i_0: Initial population of infected
    :param r_0: Initial population of recovered
    :param beta: const
    :param mu: const
    :return: Susceptibles through time, Infected through time
    """

    S = []
    I = []
    R = []
    T = []
    S.append(s_0)
    I.append(i_0)
    R.append(r_0)
    T.append(0)
    u0 = np.exp(-beta * r_0 / gamma)
    j = 0
    for j in range(total_time):
    #while j < 100:
        #N = S[j] + I[j] + R[j]
        N = s_0 + i_0 + r_0
        c = -beta * N
        u = (-beta/gamma) * R[j]
        #u = u0 + 0.01
        #t = (u - u0) / 2 * (f(u0, c, gamma, beta, s_0) + f(u, c, gamma, beta, s_0))
        T.append(j)
        S.append(s_0 * u)
        I.append((gamma / beta) * np.log(u) - s_0 * u - c/beta)
        R.append((-gamma / beta) * np.log(u))
        #u0 = copy.copy(u)

    return [T, S, I, R]


def SIS_sol(s_0, i_0, r, alpha, total_time, total_number_of_steps):

    """

    :param s_0: Intial population of susceptible
    :param i_0: Intial population of infected
    :param r:
    :param alpha:
    :param total_time: total simulation time
    :param total_number_of_steps: int, total number of steps in the sim
    :return: Susceptibles through time, Infected through time
    """

    S = []
    I = []
    #S.append(s_0)
    #I.append(i_0)
    time = np.linspace(0, total_time, total_number_of_steps+1)
    k = s_0 + i_0
    for index, t in enumerate(time):
        beta = r * k - alpha
        c = (beta - i_0 * r) / (beta * i_0)
        I.append(beta / (r + beta * c * np.exp(-beta * t)))
        S.append(k - beta / (r + beta * (beta - i_0 * r) / (beta * i_0) * np.exp(-beta * t)))
        k = S[index] + I[index]

    return [S, I, time]

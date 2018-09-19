#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: jl
"""
# This program has 2 functions which calculate the solutions of the SIR and SIS
# model presented in Shabbir et al. A note on Exact solution of SIR and SIS epidemic models
# https://arxiv.org/pdf/1012.5035.pdf
import numpy as np

def SIR_sol(s_0, i_0, r_0, beta, mu, total_time):

    """
    :param s_0: Initial population of susceptibles
    :param i_0: Initial population of infected
    :param r_0: Initial population of recovered
    :param beta: const
    :param mu: const
    :return: S, I
    """

    C = s_0 + i_0 - 1
    lambd = beta - mu + beta*C
    D = (lambd - i_0 * beta) / (lambd*i_0 * np.exp(beta * C / mu))

    S =[]
    I = []
    S.append(s_0)
    I.append(i_0)

    for t in range(0, total_time):

        param = beta + lambd * D * np.exp(- lambd * t) * np.exp(beta * C / mu)
        S.append((1 + (s_0 + i_0 -1) * (1 - mu * t) - lambd/param))
        I.append(lambd/param)
    
    return [S, I]

def SIS_sol(s_0, i_0, r, alpha, total_time):

    S = []
    I = []
    S.append(s_0)
    I.append(i_0)

    for t in range(total_time):
        k = S[t] + I[t]
        beta = r * k - alpha
        c = (beta - i_0) / (beta * i_0)
        I.append(beta / (r + beta * c * np.exp(-beta * t)))
        S.append(k - beta / (r + beta * (beta - i_0 * r) / (beta * i_0) * np.exp(-beta * t)))

    return [S, I]
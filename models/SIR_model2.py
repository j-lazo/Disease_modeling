#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: jl
"""

def SIR_model2(t, x, c):
    
    # ---parameters needed---

    beta = c[0]
    gamma = c[1]
    R0 = beta/gamma
    
    # ---initial conditions---
    
    S = x[0]
    I = x[1] 
    R = x[2]
    
    # ---total number of individuals---
    N = I+S+R   
    
    # --- the system ---

    #dS = -beta*S*I/N - gamma*S
    dS = -beta*S*I
    dI = beta*(S*I) - gamma*I
    dR = gamma*I

    return [dS, dI, dR]     

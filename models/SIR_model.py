# -*- coding: utf-8 -*-
"""
@author: jl
"""

def SIR_model(t, x, c):
    
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
    
    dS = -beta*S*I - gamma*S + gamma
    dI = beta*(S*I) - gamma*I
    dR = gamma*I

    return [dS, dI, dR]     

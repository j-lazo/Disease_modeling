#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:43:06 2018

@author: jl
"""

def SIR_model(t, x, c=[0.1, 0.1]):
    
    # ---parameters needed---

    beta = c[0]
    gamma = c[1]
    R0 = beta/gamma
    
    # ---initial conditions---
    
    I = x[0]
    S = x[1] 
    R = x[2]
    
    # ---total number of individuals---
    N = I+S+R   
    
    # --- the system ---
    
    dS = -beta*S*I/N - gamma*S + gamma
    dI = beta*(S*I)/N - gamma*I    
    dR = gamma*I

    return [dS, dI, dR]     

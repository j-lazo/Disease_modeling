#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: jl
"""
import numpy as np


def SI_model2(t, x, c=[1, 1.3, 0.3]):
    
    # ---parameters needed---

    alpha = c[0]
    beta0 = c[1]
    ep = c[2]
    
    beta = beta0*(1+ep*np.cos(2*np.pi*t/365))
    R0 = 1/alpha*beta
    
    # ---initial conditions---
    
    s1 = x[0]
    i1 = x[1] 
    
    # ---total number of individuals---
    N = s1 + i1   
    
    # --- the system ---
    
    ds1 = -beta*s1*i1/N
    di1 = beta*(s1*i1)/N - alpha*i1    
        
    return [ds1, di1]     

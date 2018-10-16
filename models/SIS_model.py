#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: jl
"""
import numpy as np


def SIS_model(t, x, c):
    
    # ---parameters needed---

    beta = c[0]
    alpha = c[1]
    
    R0 = 1/alpha*beta
    
    # ---initial conditions---
    
    s1 = x[0]
    i1 = x[1] 
    
    # ---total number of individuals---
    N = s1 + i1   
    
    # --- the system ---
    
    ds1 = -beta*s1*i1 + alpha*i1
    di1 = beta*(s1*i1) - alpha*i1
        
    return [ds1, di1]     

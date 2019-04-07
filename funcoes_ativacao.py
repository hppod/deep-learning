# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:01:53 2019

@author: mmpod
"""

import numpy as np
#transfer function

def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

def tahnFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

sF = stepFunction(20)
sigF = sigmoidFunction(0.358)
thF = tahnFunction(0.358)
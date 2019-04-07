# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:01:53 2019

@author: mmpod
"""

import numpy as np
#transfer function

#usada para problemas linearmente separaveis
def stepFunction(soma):
    if(soma >= 1):
        return 1
    return 0

#utilizada para classificação binaria
def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

#classificação entre -1 e 1
def tahnFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

#utilizada em redes neurais convolucionais ou muitas camadas
def reluFunction(soma):
    if soma >= 0:
        return soma
    return 0

#passa o valor pra frente, usada em regressão
def linearFunction(soma):
    return soma

#usada em classificação com mais valores
def softMaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()

sF = stepFunction(20)
sigF = sigmoidFunction(0.358)
thF = tahnFunction(0.358)
rF = reluFunction(0.358)
lF = linearFunction(1)

valores = [5.0, 2.0, 1.3]
print(softMaxFunction(valores))
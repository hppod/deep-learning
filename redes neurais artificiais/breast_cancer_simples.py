# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:46:26 2019

@author: mmpod
"""

import pandas as pd

previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25)
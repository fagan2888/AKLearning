# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:43:18 2013

@author: dgevans
"""
from primitives import parameters
import bellman
import numpy as np

Para = parameters()
Para.gamma = 2
#Para.z = np.array([1.03,0.99,0.9])
S = 3
p_d = np.linspace(0.05,0.95,1000)
Para.q[2] = 2.0
Para.q[0] = 0.5
c = np.zeros((len(p_d),S))
g = np.zeros((len(p_d),S))
V = np.zeros((len(p_d),S))

for s in range(0,S):
    V[:,s],c[:,s],g[:,s] =zip(* map(lambda p: bellman.solveBellman(Para,p,s),p_d) )

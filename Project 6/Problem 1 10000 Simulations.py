# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:35:32 2017

@author: Matthew Kim
EE381 Project 6
Problem 1 10000 simulations
"""

import numpy as np
from matplotlib import pyplot as plt

N = 10000
n = 15      # Number of transitions to be computed
X = np.char.array(np.zeros((n,N)))
M = np.zeros((n,3))
#
p11 = 1/3; p12 = 1/3; p13 = 1/3;  # Transition probabilities
p21 = 1/2; p22 = 0; p23 = 1/2;
p31 = 1/4; p32 = 1/4; p33 = 1/2;
#
d01 = 1/4; d02 = 1/2; d03 = 1/4;  # Probability distribution for initial state
#
for k in range(0,N) :
    r0 = np.random.rand()  # Calculate initial state
    if  r0<=d01 : 
        s0 = 'R'
    elif (r0>d01 and r0<=d01+d02) :
        s0 = 'N'
    elif r0>d01+d02 :
        s0 = 'S'
    X[0,k] = s0
#
for k in range(0,N) :
    for j in range(1,n) :
        sp = X[j-1,k]
        r = np.random.rand()
        if sp==b'R' :
            if r<=p11 :
                s = 'R'
            elif (r>p11 and r<=p11+p12) :
                s = 'N'
            elif r>p11+p12 :
                s = 'S'
        elif sp==b'N' :
            if r<=p21 :
                s = 'R'
            elif (r>p21 and r<=p21+p22) :
                s = 'N'
            elif r>p21+p22 :
                s = 'S'
        elif sp==b'S' :
            if r<=p31 :
                s = 'R'
            elif (r>p31 and r<=p21+p32) :
                s = 'N'
            elif r>p31+p32 :
                s = 'S'
        X[j,k] = s
#
for j in range (0, n) :
    x = X[j,:]
    ma = len(x.find(x==b'R'))
    mb = len(x.find(x==b'N'))
    mc = len(x.find(x==b'S'))
    M[k,:] = [ma, mb, mc]
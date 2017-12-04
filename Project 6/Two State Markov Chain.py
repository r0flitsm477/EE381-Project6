# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:01:34 2017
Two State Markov Chain
@author: Matthew
"""

import numpy as np
from matplotlib import pyplot as plt

N = 10000   # Number of experiments
n = 15      # Number of transitions to be computed
X = np.char(np.zeros((n,N)))    # Each column of X represents one of the N experiments
M = np.zeros((n,3))             # M contains the experimental probabilities for states A & B
S = np.char(n,1);               # Initialize state array
#
p11 = 0.8; p12 = 0.2;
p21 = 0.5; p22 = 0.5;
#
d01 = 0.4; d02 = 0.6;
#
for j in range (1, 1) :
    r0 = np.rand();   # Calculate initial state
    if  r0<=d01 : 
        s0 = 'A'
    elif r0>d01 :
        s0 = 'B'
    S[1] = s0;        # Initial state
#
for k in range (1, n-1):
    s = S[k]
    r = np.rand();
    if s=='A' :
        if r<=p11 :
            S[k+1] = 'A'
        elif r>p11 :
            S[k+1] = 'B'
    elif s=='B' :
        if r<=p21 :
            S[k+1] = 'A'
        elif r>p21 :
            S[k+1] = 'B'
    X[:,j] = S
"""
for j in range (1, n) :
    # x = X(j,:)
    ma = length(find(x=='A'))
    mb = length(find(x=='B'))
    # M(j,:)=[ma mb]/N
"""
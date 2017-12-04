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
"""
X = np.char.array(np.zeros((n,N)))  # Each column of X represents one of the N experiments
M = np.zeros((n,3))                 # M contains the experimental probabilities for states A & B
S = np.char.array(1,n);             # Initialize state array
"""
#
p11 = 0.8; p12 = 0.2;
p21 = 0.5; p22 = 0.5;
#
d01 = 0.4; d02 = 0.6;
#
A = []
B = []
S = []
r0 = np.random.rand()
if  r0<=d01 : 
    S.append('A')
    A.append(1)
    B.append(0)
elif r0>d01 :
    S.append('B')
    A.append(0)
    B.append(1)
#
for k in range(1, n) :
    s = S[k-1]
    r = np.random.rand()
    if s == 'A' :
        if  r<=p11 : 
            S.append('A')
            A.append(1)
            B.append(0)
        elif r>p11 :
            S.append('B')
            A.append(0)
            B.append(1)
    elif s == 'B' :
        if  r<=p21 : 
            S.append('A')
            A.append(1)
            B.append(0)
        elif r>p21 :
            S.append('B')
            A.append(0)
            B.append(1)

fig1 = plt.figure(1)
StateA = plt.plot(A, '--*', label='State A')
StateB = plt.plot(B, '--o', label='State B')
plt.title('Two-state Markov Chain: Single Run')
plt.xlabel('Time step(n)')
plt.ylabel('State')
plt.legend()
    
"""
r0 = np.random.rand()   # Calculate initial state
if  r0<=d01 : 
    s0 = 'A'
elif r0>d01 :
    s0 = 'B'
S[1] = s0;              # Initial state
#
for k in range (1, n-1):
    s = S[k]
    r = np.random.rand();
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
    X[:,k] = S
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:35:32 2017

@author: matth
Problem 1 10000 simulations
"""

import numpy as np
from matplotlib import pyplot as plt

N = 10000
n = 15      # Number of transitions to be computed
#
p11 = 1/3; p12 = 1/3; p13 = 1/3;  # Transition probabilities
p21 = 1/2; p22 = 0; p23 = 1/2;
p31 = 1/4; p32 = 1/4; p33 = 1/2;
#
d01 = 1/4; d02 = 1/2; d03 = 1/4;  # Probability distribution for initial state
#
R = np.zeros(n)
N = np.zeros(n)
S = np.zeros(n)
State = ['0'] * 15
#
r0 = np.random.rand()  # Calculate initial state
if  r0<=d01 : 
    State[0] = 'R'
    R[0] = 1
elif (r0>d01 and r0<=d01+d02) :
    State[0] = 'N'
    N[0] = 1
elif r0>d01+d02 :
    State[0] = 'S'
    S[0] = 1
#
for k in range (1, n):
    s = State[0]
    r = np.random.rand()
    if s=='R' :
        if r<=p11 :
            State[k] = 'R'
            R[k] = 1
        elif (r>p11 and r<=p11+p12) :
            State[k] = 'N'
            N[k] = 1
        elif r>p11+p12 :
            State[k] = 'S'
            S[k] = 1
    elif s=='N' :
        if r<=p21 :
            State[k] = 'R'
            R[k] = 1
        elif (r>p21 and r<=p21+p22) :
            State[k] = 'N'
            N[k] = 1
        elif r>p21+p22 :
            State[k] = 'S'
            S[k] = 1
    elif s=='S' :
        if r<=p31 :
            State[k] = 'R'
            R[k] = 1
        elif (r>p31 and r<=p21+p32) :
            State[k] = 'N'
            N[k] = 1
        elif r>p31+p32 :
            State[k] = 'S'
            S[k] = 1
#
fig1 = plt.figure(1)
Rain = plt.plot(R, '--*', label='Rain')
Nice = plt.plot(N, '--o', label='Nice')
Snow = plt.plot(S, '--+', label='Snow')
plt.title('Three-state Markov Chain: Single Run')
plt.xlabel('Time step(n)')
plt.ylabel('State')
plt.legend()
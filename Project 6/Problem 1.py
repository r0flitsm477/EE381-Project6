# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:39:58 2017
EE 381 Project 6
Problem 1 - Three State Markov Chain
@author: Matthew
"""

import numpy as np
from matplotlib import pyplot as plt

N = 10000   # Number of experiments
n = 15      # Number of transitions to be computed
X = np.char.array(np.zeros((n,N)))      # Each column of X represents one of the N experiments
M = np.zeros((n,3))                     # M contains the experimental probabilities for states A & B
S = np.char.array(n,1);                 # Initialize state array
#
p11 = 1/3; p12 = 1/3; p13 = 1/3;  # Transition probabilities
p21 = 1/2; p22 = 0; p23 = 1/2;
p31 = 1/4; p32 = 1/4; p33 = 1/2;
#
d01 = 1/4; d02 = 1/2; d03 = 1/4;  # Probability distribution for initial state
#
for j in range (1, N) :
    r0 = np.random.rand();  # Calculate initial state
    if  r0<=d01 : 
        s0 = 'R'
    elif (r0>d01 and r0<=d01+d02) :
        s0 = 'N'
    elif r0>d01+d02 :
        s0 = 'S'
    S[1] = s0;              # Initial state
#
for k in range (1, n-1):
    s = S[k]
    r = np.rand();
    if s=='R' :
        if r<=p11 :
            S[k+1] = 'R'
        elif (r>p11 and r<=p11+p12) :
            S[k+1] = 'N'
        elif r>p11+p12 :
            S[k+1] = 'S'
    elif s=='N' :
        if r<=p21 :
            S[k+1] = 'R'
        elif (r>p21 and r<=p21+p22) :
            S[k+1] = 'N'
        elif r>p21+p22 :
            S[k+1] = 'S'
    elif s=='S' :
        if r<=p31 :
            S[k+1] = 'R'
        elif (r>p31 and r<=p21+p32) :
            S[k+1] = 'N'
        elif r>p31+p32 :
            S[k+1] = 'S'
    X[:,j] = S
#
for j in range (1, n) :
    x = X[j,:]
    ma = len(str.find(x=='R'))
    mb = len(str.find(x=='N'))
    mc = len(str.find(x=='S'))
    M[j,:] = [ma, mb, mc]/N
#
nv = range(0, n-1)
fig1 = plt.figure(1)
plt.plot(nv, M[:,1], '*:', 
         nv, M[:,2], '+:', 
         nv, M[:,3], '^:')
plt.title('Simulation Results -- States R, N, S')
plt.xlabel('Time step(n)')
plt.ylabel('Prob(State)')
plt.legend('State R', 'State N', 'State S')
#
P = np.matrix([p11, p12, p13],
              [p21, p22, p23],
              [p31, p32, p33])
y0 = [1/4, 1/2, 1/4]
Y = np.zeros((n,3))
Y[1,:] = y0
for k in range(1, n-1) :
    Y[k+1,:] = Y[k,:]*P
#
fig2 = plt.figure(2)
plt.plot(nv, Y[:,1], 'o:', 
         nv, Y[:,2], 'o:', 
         nv, Y[:,3], 'o:')
plt.title('Results based on State Transition Matrix -- States R, N, S')
plt.xlabel('Time step(n)')
plt.ylabel('Prob(State)')
plt.legend('State R', 'State N', 'State S')
#
fig3 = plt.figure(3)
plt.plot(nv, M[:,1], '*', nv, Y[:,1], 'o:', 
         nv, M[:,2], '*', nv, Y[:,2], 'o:',
         nv, M[:,3], '*', nv, Y[:,3], 'o:')
plt.title('Comparison: Experimental simulation & State transition matrix')
plt.xlabel('Time step (n)')
plt.ylabel('Prob(State)')
plt.legend('Experimental simulation', 'State transition matrix')
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:23:57 2017

@author: Matthew Kim
EE381 Project 6
Problem 2 Google Page Rank
"""

import numpy as np
from matplotlib import pyplot as plt

n = 20
#
p11 = 0;   p12 = 1;   p13 = 0;   p14 = 0;   p15 = 0;
p21 = 1/2; p22 = 0;   p23 = 1/2; p24 = 0;   p25 = 0;
p31 = 1/3; p32 = 1/3; p33 = 0;   p34 = 0;   p35 = 1/3;
p41 = 1;   p42 = 0;   p43 = 0;   p44 = 0;   p45 = 0;
p51 = 0;   p52 = 1/3; p53 = 1/3; p54 = 1/3; p55 = 0;
#
v1 = [1/5, 1/5, 1/5, 1/5, 1/5]
v2 = [0, 0, 0, 0, 1]
#
nv = range(0,n)
P = np.matrix([[p11, p12, p13, p14, p15],
               [p21, p22, p23, p24, p25],
               [p31, p32, p33, p34, p35],
               [p41, p42, p43, p44, p45],
               [p51, p52, p53, p54, p55]])
P1 = P
P2 = P
#
Y1 = np.zeros((n,5))
Y2 = np.zeros((n,5))
Y1[0,:] = v1
Y2[0,:] = v2
for k in range(1,n) :
    Y1[k,:] = Y1[k-1,:]*P1
    Y2[k,:] = Y2[k-1,:]*P2
#
print(Y1)
print(Y2)
#
fig1 = plt.figure(1)
plt.plot(nv, Y1[:,0], '--*', label='A')
plt.plot(nv, Y1[:,1], '--o', label='B')
plt.plot(nv, Y1[:,2], '--+', label='C')
plt.plot(nv, Y1[:,3], '--.', label='D')
plt.plot(nv, Y1[:,4], '--,', label='E')
plt.title('Results based on State Transition Matrix -- v1')
plt.xlabel('Time step(n)')
plt.ylabel('Prob(State)')
plt.legend()
#
fig2 = plt.figure(2)
plt.plot(nv, Y2[:,0], '--*', label='A')
plt.plot(nv, Y2[:,1], '--o', label='B')
plt.plot(nv, Y2[:,2], '--+', label='C')
plt.plot(nv, Y2[:,3], '--.', label='D')
plt.plot(nv, Y2[:,4], '--,', label='E')
plt.title('Results based on State Transition Matrix -- v2')
plt.xlabel('Time step(n)')
plt.ylabel('Prob(State)')
plt.legend()
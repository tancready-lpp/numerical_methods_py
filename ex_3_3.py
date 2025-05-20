#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:33:48 2024

@author: tancredi

Esercizio 3.3 pg 68 Manuale "Numerical Methods for Astrophysics"

Prompt:
    
Produce a new contour map of the mass of the secondary black hole (i.e. the lighter one) versus the mass of the primary black hole (i.e. the more massive one) considering a sample of theoretically generated binary black holes. Unlike the previous exercise, here you have to generate the matrix z (containing the number of binary black holes in each cell with primary mass between m1 + δm and m1 − δm with δm = 0.5 M⊙ and with secondary mass between m2 + δm and m2 − δm with δm = 0.5 M⊙). The file you should start from is time_BHillustris1_30.dat (look at the comments in the first line to understand the meaning of the columns). Columns 7 and 8 are the masses of the two black holes. Note that the black hole in column 7 is not necessarily the most massive: you should swap the two black holes if the one in column 7 is lighter than the one in column 8. If you succeed, you should be able to recover a contour plot as the one in Figure 19 pag 69.

"""


# TO BE FINISHED

import numpy as np
import matplotlib.pyplot as plt
import time
import pdb


start = time.time()

path = r"/Users/tancredi/Desktop/python/corso UNIPD/examples/exercisespython-20240724/"

m1, m2 = np.genfromtxt(path + r"time_BHillustris1_30.dat", usecols=(6,7), unpack = True)

diff = m1-m2

dm = 0.5

xbins = np.arange(min(m1), max(m1), step = dm)
ybins = np.arange(min(m2), max(m2), step = dm)

bins = (xbins, ybins)

hist, xedg, yedg = np.histogram2d(m1,m2, bins = bins)
hist = np.where(hist == 0, 1, hist)
hist = hist.T  #transpose the matrix

# hist = np.reshape(hist(1,(len(xedg)-1)*(len(yedg)-1)))
        
hist = np.log10(hist)

xb = np.zeros(len(xedg)-1)
yb = np.zeros(len(yedg)-1)

for i in range(len(xedg)-1):
    xb[i] = (xedg[i]+xedg[i+1])/2.
    
for j in range(len(yedg)-1):
    yb[j] = (yedg[j]+yedg[j+1])/2.

cf = plt.contourf(xb, yb, hist, levels=20)
plt.xlabel("$M1 [M_{\odot}]$")
plt.ylabel("$M2 [M_{\odot}]$")
plt.colorbar(cf,  label = "$N_{merg}$", format = '$10^{x:.0f}$')
plt.title("Exercise 3.3 pag. 68")

plt.show()

end = time.time()

print(f"Computational time = {end-start:.3f}s")

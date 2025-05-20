#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:30:56 2024

@author: tancredi

Esercizio 3.2 pg 68 Manuale "Numerical Methods for Astrophysics"

Prompt:
    
Produce a contour map like Fig. 18 pg 67 with data files chirpmass_bin.dat (array of chirp masses, M⊙), tmerg_bin.dat (array of merger times, Gyr), chirpmass_tmerg_tot.dat (complete matrix to produce the contours).
"""

import numpy as np
import matplotlib.pyplot as plt

# sys.path.append('/Users/tancredi/Desktop/python/corso UNIPD/examples/exercisespython-20240724')
path = "/Users/tancredi/Desktop/python/corso UNIPD/examples/exercisespython-20240724/"


m_chirp = np.genfromtxt(path + "chirpmass_bin.dat")
t_merg = np.genfromtxt(path+"tmerg_bin.dat")
data = np.genfromtxt(path + "chirpmass_tmerg_tot.dat")

data = np.log10(data)

cf = plt.contourf(t_merg,m_chirp, data, levels = 100, cmap = 'plasma')
cl = plt.contour(t_merg,m_chirp, data, levels = 12, colors = "k", linewidths = 0.2)

t = [l for l in np.linspace(0, data.max(), 6)] # NB: min(data) gives an error, use array.min() 
plt.colorbar(cf, label = "$N_{merg}$", ticks = t, format = '$10^{x:.0f}$')
# plt.clabel(cl)

plt.ylim(0,40)
plt.xlabel("$t_{merge} [Gyr]$")
plt.ylabel("$M_{chirp} [M_{\odot}]$")
plt.title("Exercise 3.2 pag. 68")

plt.show()
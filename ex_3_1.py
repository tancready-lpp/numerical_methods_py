#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:18:21 2024

@author: tancredi

Esercizio 3.1 pg 54 Manuale "Numerical Methods for Astrophysics"

Prompt:
    
Write a script to plot comoving distance, luminosity distance and look- back time as a function of redshift. The results should look like Figure 13 pg 58.
"""

from math import sqrt
from scipy.integrate import quad # quad returns a tuple: quad(f, a, b) -> (integral, error)
import matplotlib.pyplot as plt

# Defining constants
c = 3e5 # km/s Speed of light
H0 = 67.2 # km/s/Mpc Hubble constant
OmegaM = 0.2726  # omega matter, parameter from cosmology
OmegaL = 0.7274  # omega lambda, parameter from cosmology
convert=1e5/3.086e24*3.1536e7*1e9  # converts from km/s/Mpc to Gyr

redshift = [x/10. for x in range(0,300)]

Ilb = lambda x: (1./H0) * 1./(sqrt((OmegaM*(1. + x)**3.)  + OmegaL) * (1. + x))

Id = lambda x: (c/H0) * 1./sqrt((OmegaM*(1. + x)**3.)  + OmegaL)

tlb = []
Dc = []
Dl = []

for z in redshift:
    tlb.append(quad(Ilb, 0, z)[0] / (H0*convert))
    dc_value = quad(Id, 0.0, z)[0] / 1e3  # converting to Gpc
    Dc.append(dc_value) # Comoving Distance in Mpc
    Dl.append((1+z)*dc_value) # Lumosity Distance in Mpc
    

# plt.plot(redshift,tlb, 'b-')

plt.xlabel("Redshift")
plt.ylabel("Lookback Time (Gyr)")
plt.title("Exercise 3.1.2 pag. 54")

plt.plot(redshift,Dc, 'r', label = "Dc")
plt.plot(redshift,Dl, 'b--',label = "Dl") 

plt.ylim(0,150)

plt.xlabel("Redshift")
plt.ylabel("Dc, Dl [Gpc]")

# plt.legend()

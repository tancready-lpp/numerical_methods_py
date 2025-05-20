#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:45:59 2024

@author: tancredi

Esercizio 2.2 pg 39 Manuale "Numerical Methods for Astrophysics"

Prompt:
    
Write a python script to calculate the comoving distance and the luminosity distance given the redshift. Use scipy.integrate.quad for the integration

"""

from math import sqrt
from scipy.integrate import quad # quad returns a tuple: quad(f, a, b) = (integral, error)

# Defining constants
c = 3e5 # km/s Speed of light
H0 = 67.2 # km/s/Mpc Hubble constant
OmegaM = 0.2726  #omega matter, parameter from cosmology
OmegaL = 0.7274  #omega lambda, parameter from cosmology

z = float(input("Select the inital Redshift z = " ))

I = lambda x: (c/H0) * 1./sqrt((OmegaM*(1. + x)**3.)  + OmegaL)

Dc = quad(I, 0.0, z)[0]
Dl = (1+z)*Dc

print(f"Comoving distance Dc(z={z:.1f}) = {Dc:.0f}Mpc")
print(f"Luminosity distance Dc(z={z:.1f}) = {Dl:.0f}Mpc")
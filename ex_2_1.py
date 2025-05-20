#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:58:49 2024

@author: tancredi

Esercizio 2.1 pg 21 Manuale "Numerical Methods for Astrophysics"

Prompt:
    
Calculate the distance covered in a (user provided) time t by a ball falling from a tower of (user provided) height h. Furthermore, calculate at what time t2 the ball reaches the ground (the gravity constant g = 9.81 m s−2).

"""

import math

t = float(input("Select the time for which the ball is falling in seconds: t = "))
h = float(input("Select the height from which the ball is falling in meters: h = "))

g = 9.81 # m/s^2

d = 0.5 * g * t**2 # Distance fallen in t seconds

t_ground = math.sqrt(2*h/g) # Time to reach the ground

print(f"The distance covered in {t:.2f}s is {d:.2f}m")
print(f"The time to reach the ground from {h:.2f}m is {t_ground:.2f}s")

if t_ground<=t:
    print("The ball has already reached the ground by the selected time t!")
else:
    print("The ball has still to fall before touching the ground!")
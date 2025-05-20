"""Write a python script to implement the Euler’s method,
the midpoint method and the fourth-order Runge-Kutta method. 
Use this script to integrate the following differential equation:

dx/dy = −x^3 + sin t

Compare the results. 
For a choice of initial time t0 = 0.0, final time tfin = 100, initial position x(t0) = 0.0 and step-size h = 0.4"""

import math
import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return x**3 - np.sin(t)

def euler(x,t):
    h = 0.1
    x_new = x + h*f(x,t) 
    return x_new

def midpoint(x,t):
    h = 0.1
    k1 = (h/2)*f(x,t) 
    k2 = h*f(x+h,t+h/2)
    x_new = x + k2
    return x_new

def rungekutta4(x,t):
    h = 0.1
    k1 = (h/2)*f(x,t) 
    k2 = h*f(x+h,t+h/2)/2
    k3 = h*f(x+k2,t+h/2)
    k4 = h*f(x+k3, t+h)
    x_new = x + (2*k1 +4*k2 + 2*k3 + k4)
    return x_new

t_vec = np.linspace(0,100, 1000)
# print(t)
x_eul = np.zeros(len(t_vec))
x_mid = np.zeros(len(t_vec))
x_rk = np.zeros(len(t_vec))
# print(x)

for i,t in enumerate(t_vec):
    x_eul[i] = euler(x_eul[i],t)
    x_mid[i] = midpoint(x_mid[i],t)
    x_rk[i] = rungekutta4(x_rk[i],t)
    
plt.title("Ordinary differential eq solving methods $ dx/dt = x^3 - sin(t)$")
plt.plot(t_vec, x_eul, label = "Euler method")
plt.plot(t_vec, x_mid, label = "Midpoint method")
plt.plot(t_vec, x_rk, label = "Runge Kutta 4 method")
plt.xlabel("Time [s]")
plt.legend()    
plt.show()

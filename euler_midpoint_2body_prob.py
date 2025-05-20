"""
Write a new script to implement Euler’s method to evolve a system of two points in two dimensions (xy plane), 
subject to gravity forces, with the following initial conditions.
Initial positions of particles 1 and 2 (in the plane xy): x = (1.0, -1.0), y = (1.0, -1.0). 
x1 = (1.0,1.0) v1 = (-0.5, 0.0)
x1 = (-1.0,-1.0) v2 = (0.5, 0.0)
Initial velocities of particles 1 and 2 (in the plane xy): vx = (-0.5, 0.5), vy = (0.0, 0.0).

Let us assume that the masses are m1 = m2 = 1, and the gravity constant in our units is G = 1.
Let us assume t0 = 0, tfin = 300 and h = 0.01. The result should look like the blue line in Figure 42.
"""

import numpy as np

def acc(x1,x2,t):
    G =






t_vec = np.linspace(0,300, int(3e3))
h= 0.01 

x1 = [[0. for i in range(len(t_vec))] for j in range(2)] # x1[0] == x_coord_1 x1[1] == y_coord_1 
x2 = [[0. for i in range(len(t_vec))] for j in range(2)] # x2[0] == x_coord_2 x2[1] == y_coord_2
x1[0][0] = 1
x1[0][1] = 1
x2[0][0] = -1
x2[0][1] = -1

v1 = [[0. for i in range(len(t_vec))] for j in range(2)] # v1[0] == v_x_coord_1 v1[1] == v_y_coord_1 
v2 = [[0. for i in range(len(t_vec))] for j in range(2)] # v2[0] == v_x_coord_2 v2[1] == v_y_coord_2
v1[0][0] = -0.5 
x1[0][1] = 0
x2[0][0] = -0.5
x2[0][1] = 0




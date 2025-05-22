"""
Exercise 2.1: Another ball dropped from a tower

A ball is dropped from a tower of height h with initial velocity zero.
Write a program that asks the user to enter the height in meters of the tower 
and then calculates and prints the time the ball takes until it hits the ground,ignoring air resistance. 
Use your program to calculate the time for a ball dropped from a 100 m high tower.
"""

import math
h = int(input()) # h = 0.5gt^2
g= 9.81 # m/s^2

t = math.sqrt(2*h/g)
print(f"The falling time from a {h}m high tower is {t:.2f}s")

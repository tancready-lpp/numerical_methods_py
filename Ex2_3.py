"""
Exercise 2.3:
Write a program to perform the inverse operation to that of Example 2.2.
That is, ask the user for the Cartesian coordinates x, y of a point in two-dimensional space, 
and calculate and print the corresponding polar coordinates, with the angle θ given in degrees."""

import math

print("Input X:")
x = float(input())
print("Input Y:")
y = float(input())

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y,x) # look up wikipwdia's atan2 page : https://en.wikipedia.org/wiki/Atan2

print(f"Cartesian ({x},{y}) -> ({r:.2f},{theta:.2f}) Polar")

"""
Exercise 2.2: Altitude of a satellite
A satellite is to be launched into a circular orbit around the Earth
so that it orbits the planet once every T seconds.
a)
Show that the altitude h above the Earth’s surface that the satellite must have is 

h =(GMT^2/4π^2)^1/3 -R

where G = 6.67x10^-11 m3 kg^-1 s^-2 is Newton’s gravitational constant,
M = 5.97 x10^24 kg is the mass of the Earth, and R = 6371 km is its radius. 
b)
Write a program that asks the user to enter the desired value of T and then calculates and
prints out the correct altitude in meters.
c)
Use your program to calculate the altitudes of satellites that orbit the Earth once a day
(so-called “geosynchronous” orbit), once every 90 minutes, and once every 45 minutes. 
What do you conclude from the last of these calculations?
T = 1day -> h = 3.59e+07 meters (5.63 radii)
T = 90m -> h = 2.79e+05 meters (0.04 radii)
T = 1day -> h = -2.18e+06 meters (-0.34 radii)
d)
Technically a geosynchronous satellite is one that orbits the Earth once per sidereal day,
which is 23.93 hours, not 24 hours. Why is this?
And how much difference will it make to the altitude of the satellite?
h = 3.58e+07 meters (5.62 radii) -> 1% change in altitude
"""
import math
print("Enter the period T in hours:")
T = float(input())*3600
#defining constats
G = 6.67e-11 # m3 kg^-1 s^-2
M = 5.97e24 # Earth's mass [kg] 
R = 6371e3 # Earth's Radius in meters
h = math.cbrt((G*M*T**2) / (4*math.pi**2)) - R

print(f"Satellite altitute with {T}s period is {h:.2e} meters ({h/R:.2f} radii)")

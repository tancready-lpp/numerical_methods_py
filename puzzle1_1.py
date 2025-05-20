#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:39:05 2024

@author: tancredi

Advent of Code 2024!

--- Day 1: Historian Hysteria --- 

Part 1

"""
import time
import numpy as np

start = time.time()

# Data extraction and unpack
datafile = "/Users/tancredi/Desktop/python/AdventOfCode2024/data_for_puzzles/puzzle1.txt"
array1, array2 = np.genfromtxt(datafile, usecols=(0,1), unpack=True)

# Sorting
array1 = np.sort(array1)
array2 = np.sort(array2)


# Computing the distance between each corresponding element and sum them all
dist = abs(array1-array2)
tot_dist = sum(dist)

print(f"Total distance = {tot_dist}")

end = time.time()

print(f"Total computation time = {(end-start)*1000:.3f}ms")
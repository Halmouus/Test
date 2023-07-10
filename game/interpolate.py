#!/usr/bin/python3
import math

def interpolate(x, start_x, end_x, start_y, end_y):
    # Calculate the logarithmic scaling factor
    scaling_factor = math.log(end_y) / math.log(end_x)

    # Perform logarithmic interpolation
    y = start_y * (end_y / start_y) ** ((x - start_x) / (end_x - start_x)) ** scaling_factor
    return y

def mapping(x):
    return [x, int(interpolate(x, 1, 100, 1, 95))]


print(mapping(1))
print(mapping(2))
print(mapping(10))
print(mapping(25))
print(mapping(50))
print(mapping(80))
print(mapping(99))
print(mapping(100))

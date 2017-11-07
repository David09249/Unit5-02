# Created by: David Wang
# Created on: 14-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit5-02
# This program finds the largest value in an array

from copy import deepcopy
from numpy import random

def find_greatest_value(array):
    greatest_value = float(0)
    for index in array:
        if greatest_value < index:
            greatest_value = index
    return greatest_value

my_array = []
for generate_random in range(0, random.randint(1, 25)):
    my_array.append(random.randint(1, 50))
print(my_array)
print(find_greatest_value(my_array))

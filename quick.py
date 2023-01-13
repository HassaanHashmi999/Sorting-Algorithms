from random import seed
from random import randint
from unittest.mock import patch
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from ani import animate

def quickSort(array, low, high):
  
    if low >= high:
           return
    pivot = array[low]
    piv = low
    for i in range(low+1, high+1):
           if array[i] <= pivot:
               piv += 1
               array[piv], array[i] = array[i], array[piv]
           yield array
    array[low], array[piv],  = array[piv], array[low]
    yield array
    yield from quickSort(array, low, piv - 1)
    yield from quickSort(array, piv + 1, high)


list= [1,12,3,42,10,102,10,19,11,2,71,23,14,155,120,23,40,34,32,22]

print("Unsorted Array")
print(list)

N = len(list)
animate(list, quickSort(list, 0, N-1), "Quick sort", False)
from random import seed
from random import randint
from unittest.mock import patch
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
 
def radixSort(arr, exp1):
    color=[]
    x_pos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    width = 0.2
    n = len(arr)
 

    output = [0] * (n)
 

    count = [0] * (10)

    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        color.append(index % 10)
        count[index % 10] -= 1
        i -= 1
    print(color,count)

    plt.xlabel("Array Elements")
    plt.ylabel("Element Length")
    plt.xticks(x_pos,labels=arr)
    plt.title("Radix  Sort")
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
    
 
def Radix(arr):
 
   
    maxi = max(arr)
 
    
    x_pos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
   
    exp = 1
    while maxi/ exp >= 1:
        radixSort(arr, exp)
        plt.xlabel("Array Elements")
        plt.ylabel("Element Length")
        plt.xticks(x_pos,labels=arr)
        plt.title("Radix  Sort")
        plt.bar(x_pos,arr,width=0.2,color='r')
        plt.pause(5)
        plt.cla()
        exp *= 10
 

arr = [1,12,3,42,10,102,10,19,11,2,71,23,14,155,120,23,40,34,32,22]

Radix(arr)
 
for i in range(len(arr)):
    print(arr[i],end=" ")
 
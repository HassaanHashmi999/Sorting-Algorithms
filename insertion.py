from random import seed
from random import randint
from unittest.mock import patch
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
   


data = [1,12,3,42,10,102,10,19,11,2,71,23,14,155,120,23,40,34,32,22]
x_pos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for step in range(1, len(data)):
        key = data[step]
        j = step - 1
           
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key
        plt.xlabel("Array Elements")
        plt.ylabel("Element Length")
        plt.xticks(x_pos,labels=data)
        #plt.bar_label(list,patch)
        plt.title("Insertion  Sort")
        plt.bar(x_pos,data)
        plt.pause(1)
        plt.cla()
print('Sorted Array in Ascending Order:')
print(data)
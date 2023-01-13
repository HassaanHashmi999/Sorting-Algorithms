from random import seed
from random import randint
from unittest.mock import patch
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

list= [1,12,3,42,10,102,10,19,11,2,71,23,14,155,120,23,40,34,32,22]
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


x_pos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]



for z in range(1000):
    for i in range(len(list)-1,0,-1):
     for j in range(i):
         if list[j]>list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
            plt.xlabel("Array Elements")
            plt.ylabel("Size")
            plt.xticks(x_pos,labels=list)
            #plt.bar_label(list,patch)
            plt.title("Bubble Sort")
            plt.bar(list2,list)
            plt.pause(0.01)
            plt.cla()






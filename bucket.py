from random import seed
from random import randint
from unittest.mock import patch
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np



def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)
    x_pos=[1,2,3,4,5,6,7,8,9,10]

    rnge = (max_ele - min_ele) / noOfBuckets
  
    temp = []

    for i in range(noOfBuckets):
        temp.append([])
  

    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)

        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
  
        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])

    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
           

    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1
                plt.xlabel("Array Elements")
                plt.ylabel("Size")
                plt.xticks(x_pos,labels=arr)
                #plt.bar_label(list,patch)
                plt.title("BUCKET Sort")
                plt.bar(x_pos,arr)
                plt.pause(0.5)
                plt.cla()
  
  
# Driver Code
arr = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
Buckets = 5
bucketSort(arr, Buckets)
print("Sorted array: ", arr)
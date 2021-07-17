#!/usr/bin/python3.6


# file: insertionSort.py
# author: Gaurish Korpal
# purpose: apply insertion sort on arrays consisting of random numbers


import random


# insertion sort algorithm
def insertionSort(alist):
    for index in range(1, len(alist)):
        # CLRS start with 2 since their array starts with 1

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


# generate a list of 8 random numbers
alist = [random.randrange(1, 100, 1) for i in range(8)]


# building 4 differents array from the numbers generated above
# and sorting them using insertion sort
for j in range(4):
    print("Random number list", j+1, ":", alist)
    insertionSort(alist)
    print("Sorted number list", j+1, ":", alist)
    if (j != 3):
        random.shuffle(alist)
        print()

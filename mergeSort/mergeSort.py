#!/usr/bin/python3.6

# file: mergeSort.py
# author: Gaurish Korpal
# purpose: apply merge sort on arrays consisting of random numbers


import random


# merge sort algorithm
def mergeSort(alist):

    # splitting list
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # merging list
        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1

            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


# generate a list of 8 random numbers
alist = [random.randrange(1, 100, 1) for i in range(8)]


# building 4 differents array from the numbers generated above
# and sorting them using merge sort
for j in range(4):
    print("Random number list", j+1, ":", alist)
    mergeSort(alist)
    print("Sorted number list", j+1, ":", alist)
    if (j != 3):
        random.shuffle(alist)
        print()

#!/usr/bin/python3.6


# file: compareTimes.py
# author: Gaurish Korpal
# purpose: come the runtime of insertion sort and merge sort on arrays on
# different size


import datetime
import random
import copy


# insertion sort algorithm
def insertionSort(alist):
    blist = copy.deepcopy(alist)  # so that merge sort gets the same list

    start = datetime.datetime.now()

    for index in range(1, len(blist)):
        # CLRS start with 2 since their array starts with 1

        currentvalue = blist[index]
        position = index

        while position > 0 and blist[position - 1] > currentvalue:
            blist[position] = blist[position - 1]
            position = position - 1

        blist[position] = currentvalue

    elapsed = datetime.datetime.now() - start

    return int(elapsed.total_seconds() * 1000000)  # microseconds


# merge sort algorithm
def mergeSort(alist):
    start = datetime.datetime.now()

    # splitting list
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # merging list without sentinel
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

    elapsed = datetime.datetime.now() - start

    return int(elapsed.total_seconds() * 1000000)  # microseconds


# generate different size lists of random numbers
alist1 = [random.randrange(1, 1000, 1) for i in range(10)]
print("Size 10 array:", alist1)
print("Insertion sort on size 10 array", insertionSort(alist1), "microseconds")
print("Size 10 array:", alist1)
print("Merge sort on size 10 array", mergeSort(alist1), "microseconds")
print()

alist2 = [random.randrange(1, 1000, 1) for i in range(20)]
print("Insertion sort on size 20 array", insertionSort(alist2), "microseconds")
print("Merge sort on size 20 array", mergeSort(alist2), "microseconds")
print()

alist3 = [random.randrange(1, 1000, 1) for i in range(50)]
print("Insertion sort on size 50 array", insertionSort(alist3), "microseconds")
print("Merge sort on size 50 array", mergeSort(alist3), "microseconds")
print()

alist4 = [random.randrange(1, 1000, 1) for i in range(100)]
print("Insertion sort on size 100 array", insertionSort(alist4), "microseconds")
print("Merge sort on size 100 array", mergeSort(alist4), "microseconds")
print()

alist5 = [random.randrange(1, 1000, 1) for i in range(200)]
print("Insertion sort on size 200 array", insertionSort(alist5), "microseconds")
print("Merge sort on size 200 array", mergeSort(alist5), "microseconds")
print()

alist6 = [random.randrange(1, 1000, 1) for i in range(500)]
print("Insertion sort on size 500 array", insertionSort(alist6), "microseconds")
print("Merge sort on size 500 array", mergeSort(alist6), "microseconds")

#!/bin/env python
import heapq

minheap=[]
maxheap=[]

def insertInMax(i):
    heapq.heappush(maxheap, -1*i)

def getFromMaxHeap():
    return -1*maxheap[0]

def popFromMaxHeap():
    return -1*heapq.heappop(maxheap)

def insert(i):
    # determine where is element should go (minheap or maxheap)
    ItemInMaxTree = ItemInMinTree = None
    if maxheap:
        ItemInMaxTree = getFromMaxHeap()
    if minheap:
        ItemInMinTree = minheap[0]

    if ItemInMaxTree and i <= ItemInMaxTree:
        insertInMax(i)
    elif ItemInMinTree and i >= ItemInMinTree:
        heapq.heappush(minheap, i)
    elif ItemInMinTree and ItemInMaxTree:
        heapq.heappush(minheap, i) if len(maxheap) > len(minheap) else insertInMax(i)
    elif not minheap:
        heapq.heappush(minheap, i)
    elif not maxheap:
        insertInMax(i)
    else:
        print "Something is wrong. Shouldn't be here for item ", i

    print "Min:", minheap
    print "Max:", [k*-1 for k in maxheap]

    l1 = len(minheap)
    l2 = len(maxheap)
    # determine if one element has to be rebalanced
    if abs(l1 -l2) > 1:
        if l1 > l2: # MinTree needs to shed
            e = heapq.heappop(minheap)
            insertInMax(e)
        else:
            e = popFromMaxHeap()
            heapq.heappush(minheap, e)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return -1
        for i, j in map(None, nums1, nums2):
            if i: insert(i)
            if j: insert(j)

        l1 = len(minheap)
        l2 = len(maxheap)
        if abs(l1-l2) > 0:
            median = minheap[0] if l1 > l2 else getFromMaxHeap()
        else:
            median = (getFromMaxHeap()  +  minheap[0]) /2.0

        return median

a = [0, 2,4,6,8,10,14,18,22]; b = [0,1,2,3,4,5,7,9,11,13,15,17,19,21,23,25,27,29]
print Solution().findMedianSortedArrays(a,b)


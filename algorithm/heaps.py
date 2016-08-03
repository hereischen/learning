#!/usr/bin/env python
# encoding: utf-8

import heapq

def heapsort(l):
    h = []
    for value in l:
        heapq.heappush(h, value)
    print h
    return [heapq.heappop(h) for i in range(len(h))]


print heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
x = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(x)
print x
print heapq.heappop(x)
print x
print heapq.nlargest(2,x)


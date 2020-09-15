#!/usr/bin/env python
# coding: utf-8

# In[3]:


epsion = 1e-10

def sqrt(i):
    low, high = 1/i, i
    mid = (low+high)/2
    while True:
        mid = (low+high)/2
        s = mid*mid
        if s > i:
            high = mid
        else:
            low = mid
        if high-low<epsion:
            break
    return mid

sqrt(10)


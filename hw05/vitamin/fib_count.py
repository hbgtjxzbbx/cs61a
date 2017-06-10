# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:45:14 2017

@author: hbgtjxzbbx
"""

def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n-2) + fib(n-1)
        
def count(f):
        def counted(*args):
            counted.open_count += 1
            counted.call_count += 1
            #print(counted)
            #print(fib)
            counted.maxElem=max(counted.open_count,counted.maxElem)
            result= f(*args)
            counted.open_count -= 1
            return result
        counted.open_count = 0
        counted.call_count=0
        counted.maxElem=0
        return counted

def memo(f):
    cache={}
    def memorized(n):
        if n not in cache:
            cache[n]=f(n)
        return cache[n]
    return memorized
    
fib = count(fib)   # make sure here the variable name should be the "fib", or it will not cover the function fib and add count
fib(19)
print(fib.maxElem)
print(fib.call_count)
fib=count(memo(fib))
fib(19)
print(fib.maxElem)
print(fib.call_count)

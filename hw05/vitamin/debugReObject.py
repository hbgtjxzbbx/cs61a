# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:16:19 2017

@author: hbgtjxzbbx
"""

def reList(listA):
    return listA

listA=[1,2,3]
listB=reList(listA).append(3)
listC=reList(listA)
print(listA)
listC.append(3)
print(listB)
print(listC)
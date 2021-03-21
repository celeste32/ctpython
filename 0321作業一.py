# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:47:43 2021

@author: user
"""
"""
作業一
"""

import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("list  :", list1)
list2 = random.sample(range(1,49),len(list1))
print("result:", list2)
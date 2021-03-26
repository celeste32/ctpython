# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:55:22 2021

@author: abc06
"""

"""
0321 Python程式開發 105261363：作業一
"""

import random
mylist = random.sample(range(1,49),6)
print("結果：",sorted(mylist))

"""
0321 Python程式開發 105261363：作業二（未完成）
"""
#import random
#mylist = random.sample(range(1,100),10)
#print(sorted(mylist))



"""
0321 Python程式開發 105261363：作業三
"""
money = int(input('請輸入獲利金額：'))
if money <=100000:
    print(money*0.1,'您的獲利金額在10萬以內，有10%的獎金！')
elif money >= 100001 and money <= 200000:
    print((100000*0.1)+(money-100000)*0.07,'您的獲利金額在10萬~20萬內，有1萬再加上10萬*7%的獎金！')
elif money >= 200001 and money <= 400000:
    print((100000*0.1)+(100000*0.07)+(money-200000)*0.03,'您的獲利金額在20~40萬內，有1萬7再加上10萬*3%的獎金！')

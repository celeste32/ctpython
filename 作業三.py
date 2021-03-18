# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 01:33:48 2021

@author: abc06
"""
"""
105261363：作業三
"""
import random
r = random.randint(1,100)
max = 100
min = 1
print(r)    #此處印出答案供觀看
i=0
while i<5:
    guess = int(input('請輸入你要猜的數字：'))
    if guess > r:
        max = guess
        print("請在{0}~{1}之間輸入一個數字".format(min, max))
    elif guess < r:
        min = guess
        print("請在{0}~{1}之間輸入一個數字".format(min, max))
    elif guess == r:
        print('恭喜猜對了')
    i += 1
else: i == 5 #請問第五次輸入錯誤，應該如何讓檔案不要跑出"請在min~max之間輸入一個數字"的訊息？
print('銘謝惠顧，下次再來')
    
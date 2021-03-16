# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:01:21 2021

@author: abc06
"""

"""
105261363：作業一
"""
for i in range(5,0,-1):
    print(i*'*')
    continue
for i in range(0,6,1):
    print(i*'*')

"""
105261363：作業二
"""
n = int(input('輸入一個正整數:'))
for c in range(2,n):
    if n % 4 ==0:
        print('是4的倍數')
        break
    if n % c == 0:
        print('不是質數')
        break
    if n == 2:
        print('是質數')
        break
    if c == n-1:
        print('是質數')
'''
老師，這題確實不好解，我有上網查資料和大家的程式碼怎麼寫再改出我想要的東西，
對於質數判別式的最後一個式子if c == n-1:   print('是質數') 不是很明白為什
麼是寫c == n-1  有沒有其他解法或是判斷式？
'''
        
        


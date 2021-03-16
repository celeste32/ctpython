# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
"""
這是今天3/7在三民分校做的第一個Python練習
"""
'''
這是今天3/7在三民分校上的第一堂Python課程
'''

age = 25
name = "Celeste"
rate = 0.20
isCheck = True
 
print(type(age))
print(type(name))
print(type(rate)) #這個是布林值，有true和false兩種結果
print(type(isCheck))

age = "三十歲"
print(type(age))

a = 6
b = 3
print(a+b)
print(b-a)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

a = 10
b = 2
print(a>b)
print(a==(b*5))
print((a//5)==b)
print(a!=b)
print(a<=b)

a = 5
b = 10
print((a*2==b)and(b>a))
print((a>b)and(a*2!=b))
print(not(a>b))
print((a>b)or(a*2==b))

a=10
a=a+5
print(a)

a=8
a+=2
print(a)
a-=2
print(a)
a/=2
print(a)
a*=2
print(a)
a%=2
print(a)

age = 18
if(age>=18):
    print("可考駕照")
    print("可以參與公投")
print("程式執行完畢")

account = "lcc"
password = "1234"
if((account=="lcc")and(password=="1234")):
    print("登入成功")
    print("歡迎回來")
    
    score = 59
    if score >= 60:
        print("考試通過")
    else:
        print("不及格")
    print("程式執行完畢")
    
    weight = 66
    if weight >= 110:
        print("體重過重，很危險")
    elif weight >= 90:
        print("過重，應減肥")
    elif weight >= 70:
        print("多運動")
    elif weight >= 50:
        print("多吃點")
    else:
        print("太瘦了")
    print("程式執行完畢")
    
print(int("100"))
pi = float("3.14")
print(type(pi))
print(pi)
money = 199
strM = str(money)
print(strM)
a = float("3.14")
print(a)

a = float("3.14")
b = int(a)
c = type(b)
print(c)

a = float('3.14')
b = int(a)
print(b)

score = int(input("請輸入分數："))
if(score >= 60 and score<=100):
    print("可樂一罐")
    print("及格")
elif(score<60):
    print("不及格")
else:
    print("分數輸入錯誤")
    
price = 0
item = input("點餐(A,B,C)：")

item = item.upper()

if item == "A":
    price = 150
    food = input("是否加可樂(Y/N)")
    item = item.upper()
    if food == "Y":
        price += 30
elif item == "B":
    price = 210
    item = item.upper()
    q = input("捐個錢？(Y/N)")
    if q == "Y":
        money = int(input("$："))
        price += money
elif item == "C":
    price = 69
else:
    print("選項錯誤")
print(price)

print(1,2,3,4,"聯成")
print(1,2,3,4,"聯成",sep='-')
print(1,2,3,end='\n')
print("A","B","C")

a = int(input("請輸入一個數字："))
if (a % 11) == 0:
   print("這是11的倍數")
else:
   print("這不是11的倍數，餘數為：",(a%11))

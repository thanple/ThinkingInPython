#!/usr/bin/env python3
print("Hello","World","Thanple")

#一切皆是引用
a=5
b=a
a=7
print(a,b)

a="abc"
b=a
a="xyz"
print(a,b)

a = 5
b = 5
print(a is b)

#==表示值相等，is表示引用同一个对象
a = "xyz a"
b = "xyz a"
print("a==b?",a==b)
print("a is b?",a is b)

#结链比较
print("5<8<7?",5<8<7)

#数组
a=[1,2,3,"asd"]
print(a[3])

#成员操作符
p = (4,"frong",9,-33,9,2)
print("成员操作符:",3 in p,2 in p)

#条件语句
if 4>3:
	print("4>3")
if	4<3:
	print("4>3")
else:
	print("4>=3")

#for...in
for each in [1,2,3,"asd","xyz"]:
	print(each,end=" ")
print ()

#基本异常机制
s=input("enter an integer:")
try:
	i=int(s)
	print("valid integer enterd:",i)
except ValueError as err:
	print(err)

	

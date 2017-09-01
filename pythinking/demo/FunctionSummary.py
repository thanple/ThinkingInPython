#!/usr/bin/env python3

#使用*作为参数传递和被传递

def sum(a,b,c):
	return a+b+c
param = (3,4,5)
result = sum(*param)
print("@fun1:",result)

def sum(*args):
	result = 0
	for arg in args:
		result += arg
	return args[0]

result = sum(2,3,4)
print("@fun2:",result)

#默认参数
def fun1(a, * ,b=10):
	return a+b
result = fun1(5,b=6)
print("@fun3:",result)

# *作为第一个参数，**可将字典映射进行拆分*
def fun2(*,a=7,b=9):
	return a+b
option = dict(a=8,b=10)	#a,b一定需要与传递参数名称相同
result = fun2(**option)
print("@fun4:",result)

#全局变量global
def fun_temp():
	global global_param
	global_param = 10
	temp = 10
fun_temp()
print("@fun4:",global_param)#,temp)

#Lambda函数(匿名函数)
s = lambda x:"eq"if x==1 else "neq"
print("@fun5:",s(1),s(2))

elements = [(2,12,"Mg"),(1,11,"Na"),(1,3,"Li"),(2,4,"Be")]
elements.sort(key=lambda e:(-e[0],e[1]))
print("@fun6:",elements)

#断言
s = [1,2,5]
assert all(s),"0 arguments"


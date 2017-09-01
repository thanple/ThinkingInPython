#!/usr/bin/env python3

#--------------------- 复数 ---------------------
z=-89.6+2.345j
print ("z=",z.real,"+" ,z.imag)

#--------------------- 十进制数字 ---------------------
import decimal
a = decimal.Decimal(9876)
b = decimal.Decimal("54321.012345678987654321")
print("a+b=",a + b)

#--------------------- 字符串 ---------------------
#索引方式: s[start:end:step] 可缺省参数
a = "Light ray"
print("string@1:",a[::-2])
#复制
a *=  2		
print("string@2:",a)
#string.format方法
s = "The novel '{0}' was published in {year}".format("Hard Times",year=1854)
print("string@3:",s)

#格式规约
s = "The sword of truth"
s1 = "{0}".format(s)
s2 = "{0:25}".format(s)
s3 = "{0:>25}".format(s)
s4 = "{0:^25}".format(s)
s5 = "{0:-^25}".format(s)
s6 = "{0:.<25}".format(s)
s7 = "{0:.10}".format(s)
print("'"+s1+"'")
print("'"+s2+"'")
print("'"+s3+"'")
print("'"+s4+"'")
print("'"+s5+"'")
print("'"+s6+"'")
print("'"+s7+"'")

#--------------------- 元组 ---------------------
#一维元组
hair = "black","brown","bronde","red"
print("@array-1:",hair[-3:])

#二维元组
a,b = (1,2)
print("a=",a,"b=",b)
for x,y in ((1,1),(2,2),(3,9)):
	print(x,y)
#嵌套元组
things = (1,-7.5,("pea",(5,"XyZ"),"queue"))
print("@things:",things[2][1][1][2])

#命名元祖
import collections
Sale = collections.namedtuple("Sale","productid customerid date quantity price")
sales = []
sales.append(Sale(321,678,"2008-09-14",3,7.99))
sales.append(Sale(421,778,"2009-09-14",6,8.99))

total = 0
for sale in sales:
	total += sale.quantity * sale.price
print("@Total ${0:.2f}".format(total))

#******************** 列表 ********************

#带*的元祖赋值
first,*rest = [9,2,-4,8,7]
print("@first,rest=",first,rest)
#带*作为参数传递
def product(a,b,c):
	return a*b*c
L = [2,3,5]
print("@prosuct1:",product(*L) )
print("@prosuct2:",product(2,*L[1:]))


#set and list
l = list({3,2,5,7,1})	#返回[],支持l[index]
s = set(l)				#返回{},不支持s[index]
print("@set&list: ",s,l[0])

#映射类型
d1 = dict({"id":1948,"name":"Thanple","size":"3"})
del d1["size"]
for key,value in d1.items():
	print(key,":", value)
print("@dictionary getId:",d1["id"])
#默认字典也是一种字典
s = {"id":1948,"name":"Thanple","size":"3"}
print("@dictionary getId:",s["id"])

#浅拷贝与深拷贝
import copy
shallow_copy_of_dict_s = s
deep_copy_of_dict_s = copy.deepcopy(s)
s["id"] = 1949
print("@shallow copy:",shallow_copy_of_dict_s)
print("@deep copy:",deep_copy_of_dict_s)

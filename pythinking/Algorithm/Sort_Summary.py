#!/usr/bin/env python3
from Algorithm import Common
'''
	各种排序总结
'''

#快速排序：不断分成两堆，一堆比中间的值小，一堆大, 递归
def quickly_sort_partition(data,p,r):
	key = data[r]
	changer = p-1
	for visit in range(r-p):
		if(data[p+visit] <= key):
			changer += 1
			Common.exchange(data , changer , p+visit)

	Common.exchange(data , changer+1 , r)
	return changer + 1

def quickly_sort_item(data, p ,r):
	if(p < r):
		q = quickly_sort_partition(data,p,r)
		quickly_sort_item(data,p,q-1)
		quickly_sort_item(data,q+1,r)

def quickly_sort(data):
	quickly_sort_item(data,0,len(data)-1)
	return data

#计数排序：将最大值作为临时数组C长度，将C下标作为数组元素，C元素做计数，最后再还原
def counting_sort(data ,tempSize):
	#C为存放计数的数组，其下标为原数组的元素
	C = [];
	for i in range(tempSize):
		C.append(0);
	for i in range(len(data)):
		C[data[i]] += 1;

	#让临时数组C存放下标所对应的元素前面有几个元素
	for i in range(tempSize):
		C[i] += C[i-1] if i > 0 else 0   #python中的三元运算符


	#将计数数组C还原原来的数组
	B = [0]*(len(data))
	for i in range(len(data)-1,0,-1):   #逆序遍历
		B[C[data[i]]-1] = data[i]
		C[data[i]] -= 1
	return B

# 基数排序:一个数的每位依次排序
def radix_sort(data,n):
	temp = [[0 for col in range(len(data))] for row in range(10)]     #定义临时temp，存放每次临时的排序, 10行若干列
	count = [0] * 10;               #计数，存放每位排序后的个数

	for i in range(n):             #i为0表示各位，依次类推
		#根据每一位的大小存放到temp数组中
		for j in range(len(data)):
			bit = int(data[j] / (10**i)) % 10     #取每位,10**i表示10的i次幂
			temp[bit][count[bit]] = data[j]
			count[bit] += 1
		#将临时数组更新data数组，并清空
		t = 0
		for j in range(10):
			for k in range(count[j]):
				data[t] = temp[j][k]
				temp[j][k] = 0
				t += 1
			count[j] = 0
	return data


'''
	测试以上排序
'''
data = [3,5,1,6,0,4,5,3,2,8,9,6,3]
print("quikly sort: ", quickly_sort(data[:]) )

data2 = [2,5,3,0,2,3,0,3]
print("counting sort: " , counting_sort(data2[:] ,max(data2)+1 ) )

data3 = [2, 343, 342, 1, 123, 43, 4343, 433, 687, 654, 3]
print("radix sort: ",radix_sort(data3,4))


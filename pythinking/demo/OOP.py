#!/usr/bin/env python3

import collections

#通过namedtuple自定义元祖
Circle = collections.namedtuple("Circle","x y radis")
circle = Circle(13,84,9)
print("@1:",circle.x,circle.y,circle.radis)

#Point封装
from Demo import Shape

a = Shape.Point()
print(repr(a))
b = Shape.Point(3, 4)
print(str(b))		#可作为全局函数调用
print(b.distance_from_origin())
b.x = -19
print(b.__str__())	#可直接调用
print(a==b,a!=b)

#继承
p = Shape.Point(26, 45)
c = Shape.Circle(5, 28, 45)   #Circle继承了Point
print("@extends1:",p.distance_from_origin())
print("@extends2:",c.distance_from_origin())
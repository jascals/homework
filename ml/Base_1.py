# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

from numpy import *

randMat = mat(random.rand(4,4))     #生成   矩阵 
randMat.I       #矩阵求逆

# 1.数组
mm = array((1, 2, 3))
mm[0]
pp = array((2, 3, 4))
jj = array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
jj[0][1]

## 数组运算
pp + mm       #数组元素分别相加
pp * mm       #数组元素分别相乘
pp * 2        #数组元素乘二
pp ** 2       #数组元素求平方

# 2.矩阵
ss = mat((1, 2, 3))
mm = matrix((1, 2, 3))
mm[0, 1]        #区别于数组访问
pyList = [5, 4, 3]
mat(pyList)     #python数组生成矩阵
shape(mm)       #查看矩阵维数

## 矩阵运算
mm * ss.T       #乘法，ss.T是矩阵的转置
multiply(mm, ss)        #矩阵元素两两相乘

## 应用
mm.sort()       #原地排序
mm.argsort()        #得到排序后每个元素的序号
mm.mean()       #计算矩阵均值

## 多维矩阵
jj = mat([[1, 2, 3], [2, 3, 4]])
jj[1, :]        #取出第一行
jj[1, 0:2]      #去除第一行第0列和第1列的元素

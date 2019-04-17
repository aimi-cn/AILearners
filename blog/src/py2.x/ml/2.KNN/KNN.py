#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   KNN.py
@Time    :   2019/03/27 11:07:01
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   KNN近邻算法
@github  :   https://github.com/xiaoming3526/ai-ming3526
@reference:  https://github.com/apachecn/AiLearning
'''

# here put the import lib
from __future__ import print_function
from numpy import *
import numpy as np
import operator
# 导入科学计算包numpy和运算符模块operator
from os import listdir
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    """
    创建数据集和标签
    调用方式
    import kNN
    group, labels = kNN.createDataSet()
    """
    group =  array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def test1():
    group, labels = createDataSet()
    '''
    [[1.0,1.1]  #标签对应A
    [1.0,1.0]   #标签对应A
    [0,    0]   #标签对应B
    [0, 0.1]]  #标签对应B

    ['A', 'A', 'B', 'B']
    '''
    #print(str(group))
    #print(str(labels))
    #print(classify0([0.1, 0.1], group, labels, 3))
    print(classify1([0.1, 0.1], group, labels, 3))

def classify0(inX, dataSet, labels, K):
    '''
    inX: 用于分类的输入向量 输入的测试数据
    dataSet：输入的训练样本
    lables：标签向量
    k：选择最近邻居的数目 通常小于20
    注意：labels元素数目和dataSet行数相同；程序使用欧式距离公式.

    预测数据所在分类可在输入下列命令
    kNN.classify0([0,0], group, labels, 3)
    '''
    # -----------实现 classify0() 方法的第一种方式----------------------------------------------------------------------------------------------------------------------------
    # 1. 距离计算
    #计算数据大小
    dataSetSize = dataSet.shape[0]
    '''
    tile使用: 列3表示复制的行数， 行1／2表示对inX的重复的次数
    In [2]: inx = [1,2,3]
    In [3]: tile(inx,(3,1))  #列3表示复制的行数 行1表示对inX的重复的次数
    Out[3]: 
    array([[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]])

    In [4]: tile(inx,(3,2)) #列3表示复制的行数 行2表示对inX的重复的次数
    Out[4]: 
    array([[1, 2, 3, 1, 2, 3],
        [1, 2, 3, 1, 2, 3],
        [1, 2, 3, 1, 2, 3]])
    '''
    # tile生成和训练样本对应的矩阵，并与训练样本求差
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    '''
    欧氏距离： 点到点之间的距离
       第一行： 同一个点 到 dataSet的第一个点的距离。
       第二行： 同一个点 到 dataSet的第二个点的距离。
       ...
       第N行： 同一个点 到 dataSet的第N个点的距离。
    [[1,2,3],[1,2,3]]-[[1,2,3],[1,2,0]]
    (A1-A2)^2+(B1-B2)^2+(c1-c2)^2
    '''
    # 取平方
    sqDiffMat = diffMat ** 2
    # 讲矩阵的每一行相加
    sqDistances = sqDiffMat.sum(axis=1)
    # 开方
    distances = sqDistances ** 0.5
    #print ('distances=', distances)
    #distances= [1.3453624  1.27279221 0.14142136 0.1]
    # 根据距离排序从小到大的排序，返回对应的索引位置
    sortedDistIndicies = distances.argsort()
    #print ('distances.argsort()=', sortedDistIndicies)
    #distances.argsort()= [3 2 1 0]

    # 2. 选择距离最小的K个点
    classCount = {}
    for i in range(K):
        #找到该样本的类型
        voteIlabel = labels[sortedDistIndicies[i]]
        # 在字典中将该类型加一
        # 字典的get方法
        # 如：list.get(k,d) 其中 get相当于一条if...else...语句,参数k在字典中，字典将返回list[k];如果参数k不在字典中则返回参数d,如果K在字典中则返回k对应的value值
        # l = {5:2,3:4}
        # print l.get(3,0)返回的值是4；
        # Print l.get（1,0）返回值是0；
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    #print(classCount)
    #{'A': 1, 'B': 2}

    # 3. 排序并且返回出现最多的那个数据类型
    # 字典的 items() 方法，以列表返回可遍历的(键，值)元组数组。
    # 例如：dict = {'Name': 'Zara', 'Age': 7}   print "Value : %s" %  dict.items()   Value : [('Age', 7), ('Name', 'Zara')]
    # sorted 中的第2个参数 key=operator.itemgetter(1) 这个参数的意思是先比较第几个元素
    # 例如：a=[('b',2),('a',1),('c',0)]  b=sorted(a,key=operator.itemgetter(1)) >>>b=[('c',0),('a',1),('b',2)] 可以看到排序是按照后边的0,1,2进行排序的，而不是a,b,c
    # b=sorted(a,key=operator.itemgetter(0)) >>>b=[('a',1),('b',2),('c',0)] 这次比较的是前边的a,b,c而不是0,1,2
    # b=sorted(a,key=opertator.itemgetter(1,0)) >>>b=[('c',0),('a',1),('b',2)] 这个是先比较第2个元素，然后对第一个元素进行排序，形成多级排序。
    #我们现在需要出现次数最多的那个 所以使用reverse=True列表反向排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def classify1(inX, dataSet, labels, K):
    '''
    inX: 用于分类的输入向量 输入的测试数据
    dataSet：输入的训练样本
    lables：标签向量
    k：选择最近邻居的数目 通常小于20
    注意：labels元素数目和dataSet行数相同；程序使用欧式距离公式.

    预测数据所在分类可在输入下列命令
    kNN.classify0([0,0], group, labels, 3)
    '''
    # -----------实现 classify0() 方法的第二种方式----------------------------------------------------------------------------------------------------------------------------
    # 欧氏距离： 点到点之间的距离
    #    第一行： 同一个点 到 dataSet的第一个点的距离。
    #    第二行： 同一个点 到 dataSet的第二个点的距离。
    #    ...
    #    第N行： 同一个点 到 dataSet的第N个点的距离。

    # [[1,2,3],[1,2,3]]-[[1,2,3],[1,2,0]]
    # (A1-A2)^2+(B1-B2)^2+(c1-c2)^2
    
    # inx - dataset 使用了numpy broadcasting，见 https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html
    # np.sum() 函数的使用见 https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.sum.html
    # """
    #当axis为0时,是压缩行,即将每一列的元素相加,将矩阵压缩为一行
    #当axis为1时,是压缩列,即将每一行的元素相加,将矩阵压缩为一列
    # >>> np.sum([[0, 1], [0, 5]], axis=0)
    # array([0, 6])
    # >>> np.sum([[0, 1], [0, 5]], axis=1)
    # array([1, 5])
    dist = np.sum((inX - dataSet)**2, axis=1)**0.5
    
    # """
    # 2. k个最近的标签
    
    # 对距离排序使用numpy中的argsort函数， 见 https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.sort.html#numpy.sort
    # 函数返回的是索引，因此取前k个索引使用[0 : k]
    # 将这k个标签存在列表k_labels中
    # """
    k_labels = [labels[index] for index in dist.argsort()[0 : K]]
	# """
    # 3. 出现次数最多的标签即为最终类别
    
    # 使用collections.Counter可以统计各个标签的出现次数，most_common返回出现次数最多的标签tuple，例如[('lable1', 2)]，因此[0][0]可以取出标签值
	# """
    label = Counter(k_labels).most_common(1)[0][0]
    return label

if __name__ == '__main__':
    test1()
    


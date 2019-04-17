#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   KNN_demo02.py
@Time    :   2019/04/08 10:43:31
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   None
@github  :   https://github.com/xiaoming3526/ai-ming3526
'''

# here put the import lib
from __future__ import print_function
from numpy import *
# 导入科学计算包numpy和运算符模块operator
import operator
from os import listdir
from collections import Counter
import KNN

def img2vecor(filename):
    """
    将图像数据转换为向量
    :param filename: 图片文件 因为我们的输入数据的图片格式是 32 * 32的
    :return: 一维矩阵
    该函数将图像转换为向量：该函数创建 1 * 1024 的NumPy数组，然后打开给定的文件，
    循环读出文件的前32行，并将每行的头32个字符值存储在NumPy数组中，最后返回数组。
    大致流程简单解释：第一个i 每次循环一次读取一行 第一个j把第一行的i值赋值到对应的数组位置里面 eg：i=0时 lineStr=“00000000000001111000000000000000”
    returnVector[0, 32*0 + 0] = int(lineStr[0])  returnVector[0, 32*0 + 1] = int(lineStr[1]) 一直循环32次 然后i=1 继续下去
    """
    returnVector = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVector[0, 32*i+j] = int(lineStr[j])
    return returnVector

def handwritingClassTest():
    #导入数据
    hwLabels = []
    trainingFileList  = listdir('data/2.KNN/trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    # hwLabels存储0～9对应的index位置， trainingMat存放的每个位置对应的图片向量
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        # 将 32*32的矩阵->1*1024的矩阵
        trainingMat[i, :] = img2vecor('data/2.KNN/trainingDigits/%s' % fileNameStr)

    # 2. 导入测试数据
    testFileList = listdir('data/2.KNN/testDigits')  # iterate through the test set
    errorCount = 0.0
    mTest =  len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vecor('data/2.KNN/testDigits/%s' % fileNameStr)
        classifierResult = KNN.classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): 
            errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount / float(mTest)))
    
if __name__ == '__main__':
    #打开的文件名 自己修改文件路径
    filename = "data/2.KNN/trainingDigits/0_0.txt"
    #打开并处理数据
    #testVector = img2vecor(filename)
    #print(testVector)
    handwritingClassTest()

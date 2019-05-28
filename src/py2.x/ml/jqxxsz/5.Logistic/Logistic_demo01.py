#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Logistic_demo01.py
@Time    :   2019/05/27 16:31:12
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   Logistic回归案例之预测病马死亡率
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
import numpy as np
import random

'''
@description: sigmoid函数
@param  inX - 数据
@return: sigmoid函数
'''
def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))

'''
@description: 梯度上升法
@param {type} 两个参数：
第一个参数==> dataMatIn 是一个2维NumPy数组，每列分别代表每个不同的特征，每行则代表每个训练样本。
第二个参数==> classLabels 是类别标签，它是一个 1*100 的行向量。为了便于矩阵计算，需要将该行向量转换为列向量，做法是将原向量转置，再将它赋值给labelMat。
@return: 求得的权重数组(最优参数)
'''
def gradAscent(dataMatIn, classLabels):
    #用dataMatIn创建特征矩阵
    dataMatrix = np.mat(dataMatIn)
    #调换矩阵的坐标顺序，对于二维矩阵来说，transpose()就是转置 
    labelMat = np.mat(classLabels).transpose()
    #m是样本数，n是特征数
    m, n = np.shape(dataMatrix)
    #梯度上升步长
    alpha = 0.001   
    #最大迭代次数                                                     
    maxCycles = 500       
    #权重向量b，初始化为全1 这里面n为3                                                
    weights = np.ones((n,1))
    for k in range(maxCycles):
        #讲给定的值通过sigmoid函数输出为0-1之间的数值 #对w1*x1+w2*x2求对数几率回归
        h = sigmoid(dataMatrix * weights)      
        #计算真实值和预测值之间的误差                         
        error = labelMat - h
        #根据误差进行梯度更新
        weights = weights + alpha * dataMatrix.transpose() * error
    #.getA()将自身矩阵变量转化为ndarray类型的变量
    return weights

'''
@description: 改进的随机梯度上升算法
@param  dataMatrix - 数据数组
        classLabels - 数据标签
        numIter - 迭代次数
@return: weights - 求得的回归系数数组(最优参数)
'''
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    #返回dataMatrix的大小。m为行数,n为列数。
    m,n = np.shape(dataMatrix)
    #参数初始化
    weights = np.ones(n)
    # 随机梯度, 循环150,观察是否收敛
    for j in range(numIter):
        # [0, 1, 2 .. m-1]
        dataIndex = list(range(m))
        for i in range(m):
            # i和j的不断增大，导致alpha的值不断减少，但是不为0
            alpha = 4/(1.0+j+i)+0.0001
            # 随机产生一个 0～len()之间的一个值
            # random.uniform(x, y) 方法将随机生成下一个实数，它在[x,y]范围内,x是这个范围内的最小值，y是这个范围内的最大值。
            randIndex = int(np.random.uniform(0,len(dataIndex)))
            # sum(dataMatrix[i]*weights)为了求 f(x)的值， f(x)=a1*x1+b2*x2+..+nn*xn
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            #更新回归系数
            weights = weights + alpha * error * dataMatrix[randIndex]
            #删除已经使用的样本
            del(dataIndex[randIndex])
    return weights

def colicTest():
    frTrain = open('C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/5.Logistic/horseColicTraining.txt')                                        #打开训练集
    frTest = open('C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/5.Logistic/horseColicTest.txt')                                                #打开测试集
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[-1]))
    #使用梯度上升训练
    trainWeights = gradAscent(np.array(trainingSet), trainingLabels)       
    errorCount = 0; numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(np.array(lineArr), trainWeights[:,0]))!= int(currLine[-1]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec) * 100                                 #错误率计算
    print("梯度上升算法测试集错误率为: %.2f%%" % errorRate).decode('utf-8').encode('gb2312')

def colicTest1():
    frTrain = open('C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/5.Logistic/horseColicTraining.txt')                                        #打开训练集
    frTest = open('C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/5.Logistic/horseColicTest.txt')                                                #打开测试集
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[-1]))
    #使用改进的随机上升梯度训练
    trainWeights = stocGradAscent1(np.array(trainingSet), trainingLabels)       
    errorCount = 0; numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(np.array(lineArr), trainWeights))!= int(currLine[-1]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec) * 100                                 #错误率计算
    print("随机梯度上升测试集错误率为: %.2f%%" % errorRate).decode('utf-8').encode('gb2312')


def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0

if __name__ == '__main__':
    #使用梯度上升训练
    colicTest()
    #使用随机梯度上升训练
    colicTest1()
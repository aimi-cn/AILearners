#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   AdaBoost01.py
@Time    :   2019/06/24 15:18:18
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   AdaBoots元算法
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
import numpy as np
import matplotlib.pyplot as plt

'''
@description: 创建单层决策树的数据集
@param: None
@return: dataMat - 数据矩阵
        classLabels - 数据标签
'''
def loadSimpData():
    dataMat = np.matrix([[ 1. ,  2.1],
        [ 1.5,  1.6],
        [ 1.3,  1. ],
        [ 1. ,  1. ],
        [ 2. ,  1. ]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return dataMat,classLabels

'''
@description: 数据可视化
@param: dataMat - 数据矩阵
        labelMat - 数据标签 
@return: None
'''
def showDataSet(dataMat,labelMat):
    data_plus = []                                  #正样本
    data_minus = []                                 #负样本
    for i in range(len(dataMat)):
        if labelMat[i] > 0:
            data_plus.append(dataMat[i])
        else:
            data_minus.append(dataMat[i])
    data_plus_np = np.array(data_plus)                                             #转换为numpy矩阵
    data_minus_np = np.array(data_minus)                                         #转换为numpy矩阵
    plt.scatter(np.transpose(data_plus_np)[0], np.transpose(data_plus_np)[1])        #正样本散点图
    plt.scatter(np.transpose(data_minus_np)[0], np.transpose(data_minus_np)[1])     #负样本散点图
    plt.show()

'''
@description: 单层决策树分类函数
@param: dataMatrix - 数据矩阵
		dimen - 第dimen列，也就是第几个特征
		threshVal - 阈值
		threshIneq - 标志 "lt" "gt"
        这里lt表示less than，表示分类方式，对于小于阈值的样本点赋值为-1，
        gt表示greater than，也是表示分类方式，对于大于阈值的样本点赋值为-1。
@return: 
'''
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray = np.ones((np.shape(dataMatrix)[0],1))				#初始化retArray为1
    if threshIneq == 'lt':
		retArray[dataMatrix[:,dimen] <= threshVal] = -1.0	 	#如果小于阈值,则赋值为-1
    else:
		retArray[dataMatrix[:,dimen] > threshVal] = -1.0 		#如果大于阈值,则赋值为-1
    return retArray

'''
@description: 找到数据集上最佳的单层决策树
@param: dataArr - 数据矩阵
        classLabels - 数据标签
        D - 样本权重 
@return: bestStump - 最佳单层决策树信息
        minError - 最小误差
        bestClasEst - 最佳的分类结果
'''
def buildStump(dataArr,classLabels,D):
    dataMatrix = np.mat(dataArr); labelMat = np.mat(classLabels).T
    m,n = np.shape(dataMatrix)
    numSteps = 10.0; bestStump = {}; bestClasEst = np.mat(np.zeros((m,1)))
    #最小误差初始化为正无穷大
    minError = float('inf')		
    #遍历所有特征												
    for i in range(n):		
        #找到特征中最小的值和最大值												
        rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,i].max()		
        #计算步长
        stepSize = (rangeMax - rangeMin) / numSteps	
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                #计算阈值
                threshVal = (rangeMin + float(j) * stepSize)	
                #计算分类结果
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)	
                #初始化误差矩阵
                errArr = np.mat(np.ones((m,1)))
                #分类正确的,赋值为0
                errArr[predictedVals == labelMat] = 0
                #计算误差
                weightedError = D.T * errArr
                #找到误差最小的分类方式
                if weightedError < minError: 									
					minError = weightedError
					bestClasEst = predictedVals.copy()
                    #第一行的特征
					bestStump['dim'] = i
                    #阈值
					bestStump['thresh'] = threshVal
                    #标志 "lt" "gt"
					bestStump['ineq'] = inequal
    return bestStump, minError, bestClasEst

'''
@description: 使用AdaBoost算法提升弱分类器性能
@param: dataArr - 数据矩阵
		classLabels - 数据标签
		numIt - 最大迭代次数
@return: weakClassArr - 训练好的分类器
		aggClassEst - 类别估计累计值
'''
def adaBoostTrainDS(dataArr, classLabels, numIt = 40):
    weakClassArr = []
    #初始化权重
    m = np.shape(dataArr)[0]
    D = np.mat(np.ones((m, 1)) / m)
    aggClassEst = np.mat(np.zeros((m,1)))
    for i in range(numIt):
        #构建单层决策树
        bestStump, error, classEst = buildStump(dataArr, classLabels, D) 
        #计算弱学习算法权重alpha,使error不等于0,因为分母不能为0	
        alpha = float(0.5 * np.log((1.0 - error) / max(error, 1e-16)))
        #存储弱学习算法权重和单层决策树
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        #计算e的指数项
        expon = np.multiply(-1 * alpha * np.mat(classLabels).T, classEst)
        D = np.multiply(D, np.exp(expon))
        #根据样本权重公式，更新样本权重
        D = D / D.sum()
        #计算AdaBoost误差，当误差为0的时候，退出循环
        #计算类别估计累计值
        aggClassEst += alpha * classEst
        #计算误差
        aggErrors = np.multiply(np.sign(aggClassEst) != np.mat(classLabels).T, np.ones((m,1))) 	
        errorRate = aggErrors.sum() / m
        print("total error: ", errorRate)
        if errorRate == 0.0: break 
    return weakClassArr, aggClassEst

'''
@description: 分类函数
@param: datToClass - 待分类样例
		classifierArr - 训练好的分类器
@return: 分类结果
'''
def adaClassify(datToClass,classifierArr):
    dataMatrix = np.mat(datToClass)
    m = np.shape(dataMatrix)[0]
    aggClassEst = np.mat(np.zeros((m,1)))
    #遍历所有分类器，进行分类
    for i in range(len(classifierArr)):
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'], classifierArr[i]['thresh'], classifierArr[i]['ineq'])			
        aggClassEst += classifierArr[i]['alpha'] * classEst
        print(aggClassEst)
    return np.sign(aggClassEst)

if __name__ == "__main__":
    # dataArr,classLabels = loadSimpData()
    # showDataSet(dataArr,classLabels)

    # dataArr,classLabels = loadSimpData()
    # D = np.mat(np.ones((5, 1)) / 5)
    # bestStump,minError,bestClasEst = buildStump(dataArr,classLabels,D)
    # print('bestStump:\n', bestStump)
    # print('minError:\n', minError)
    # print('bestClasEst:\n', bestClasEst)

    # dataArr,classLabels = loadSimpData()
    # weakClassArr, aggClassEst = adaBoostTrainDS(dataArr, classLabels)
    # print(weakClassArr)
    # print(aggClassEst)

    dataArr,classLabels = loadSimpData()
    weakClassArr, aggClassEst = adaBoostTrainDS(dataArr, classLabels)
    print(adaClassify([[0,0],[5,5]], weakClassArr))

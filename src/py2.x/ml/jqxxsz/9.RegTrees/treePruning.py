#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   treePruning.py
@Time    :   2019/08/05 21:47:48
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   树回归之后剪枝
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
import matplotlib.pyplot as plt
import numpy as np

'''
@description: 加载数据
@param: fileName - 文件名
@return: dataMat - 数据矩阵
'''
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float, curLine))                    #转化为float类型
        dataMat.append(fltLine)
    return dataMat

'''
@description: 根据特征切分数据集合
@param: dataSet - 数据集合
        feature - 带切分的特征
        value - 该特征的值 
@return: mat0 - 切分的数据集合0
        mat1 - 切分的数据集合1
'''
def binSplitDataSet(dataSet, feature, value):
    mat0 = dataSet[np.nonzero(dataSet[:,feature] > value)[0],:]
    mat1 = dataSet[np.nonzero(dataSet[:,feature] <= value)[0],:]
    return mat0, mat1

'''
@description: 生成叶结点
@param: dataSet - 数据集合 
@return: 目标变量的均值
'''
def regLeaf(dataSet):
    return np.mean(dataSet[:,-1])

'''
@description: 误差估计函数
@param: dataSet - 数据集合
@return: 目标变量的总方差
'''
def regErr(dataSet):
    return np.var(dataSet[:,-1]) * np.shape(dataSet)[0]

'''
@description: 找到数据的最佳二元切分方式函数
@param: dataSet - 数据集合
        leafType - 生成叶结点
        regErr - 误差估计函数
        ops - 用户定义的参数构成的元组
@return: bestIndex - 最佳切分特征
        bestValue - 最佳特征值
'''
def chooseBestSplit(dataSet, leafType = regLeaf, errType = regErr, ops = (1,4)):
    import types
    #tolS允许的误差下降值,tolN切分的最少样本数
    tolS = ops[0]; tolN = ops[1]
    #如果当前所有值相等,则退出。(根据set的特性)
    if len(set(dataSet[:,-1].T.tolist()[0])) == 1:
        return None, leafType(dataSet)
    #统计数据集合的行m和列n
    m, n = np.shape(dataSet)
    #默认最后一个特征为最佳切分特征,计算其误差估计
    S = errType(dataSet)
    #分别为最佳误差,最佳特征切分的索引值,最佳特征值
    bestS = float('inf'); bestIndex = 0; bestValue = 0
    #遍历所有特征列
    for featIndex in range(n - 1):
        #遍历所有特征值
        for splitVal in set(dataSet[:,featIndex].T.A.tolist()[0]):
            #根据特征和特征值切分数据集
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
            #如果数据少于tolN,则退出
            if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN): continue
            #计算误差估计
            newS = errType(mat0) + errType(mat1)
            #如果误差估计更小,则更新特征索引值和特征值
            if newS < bestS:
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    #如果误差减少不大则退出
    if (S - bestS) < tolS:
        return None, leafType(dataSet)
    #根据最佳的切分特征和特征值切分数据集合
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    #如果切分出的数据集很小则退出
    if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):
        return None, leafType(dataSet)
    #返回最佳切分特征和特征值
    return bestIndex, bestValue

'''
@description: 树构建函数
@param: dataSet - 数据集合
        leafType - 建立叶结点的函数
        errType - 误差计算函数
        ops - 包含树构建所有其他参数的元组
@return: retTree - 构建的回归树
'''
def createTree(dataSet, leafType = regLeaf, errType = regErr, ops = (1, 4)):
    #选择最佳切分特征和特征值
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
    #r如果没有特征,则返回特征值
    if feat == None: return val
    #回归树
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    #分成左数据集和右数据集
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    #创建左子树和右子树
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree  

'''
@description: 判断测试输入变量是否是一棵树
@param: obj - 测试对象
@return: 是否是一棵树
'''
def isTree(obj):
    import types
    return (type(obj).__name__ == 'dict')

'''
@description: 对树进行塌陷处理(即返回树平均值)
@param: tree - 树
@return: 树的平均值
'''
def getMean(tree):
    if isTree(tree['right']): tree['right'] = getMean(tree['right'])
    if isTree(tree['left']): tree['left'] = getMean(tree['left'])
    return (tree['left'] + tree['right']) / 2.0

'''
@description: 后剪枝
@param: tree - 树
        test - 测试集
@return: 树的平均值
'''
def prune(tree, testData):
    #如果测试集为空,则对树进行塌陷处理
    if np.shape(testData)[0] == 0: return getMean(tree)
    #如果有左子树或者右子树,则切分数据集
    if (isTree(tree['right']) or isTree(tree['left'])):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
    #处理左子树(剪枝)
    if isTree(tree['left']): tree['left'] = prune(tree['left'], lSet)
    #处理右子树(剪枝)
    if isTree(tree['right']): tree['right'] =  prune(tree['right'], rSet)
    #如果当前结点的左右结点为叶结点
    if not isTree(tree['left']) and not isTree(tree['right']):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
        #计算没有合并的误差
        errorNoMerge = np.sum(np.power(lSet[:,-1] - tree['left'],2)) + np.sum(np.power(rSet[:,-1] - tree['right'],2))
        #计算合并的均值
        treeMean = (tree['left'] + tree['right']) / 2.0
        #计算合并的误差
        errorMerge = np.sum(np.power(testData[:,-1] - treeMean, 2))
        #如果合并的误差小于没有合并的误差,则合并
        if errorMerge < errorNoMerge:
            return treeMean
        else: return tree
    else: return tree
 
if __name__ == '__main__':
    print('\n剪枝前：')
    train_filename = 'C:\\Users\\Administrator\\Desktop\\blog\\github\\AILearners\\data\\ml\\jqxxsz\\9.RegTrees\\ex2.txt'
    train_Data = loadDataSet(train_filename)
    train_Mat = np.mat(train_Data)
    tree = createTree(train_Mat)
    print(tree)
    print('\n剪枝后：')
    test_filename = 'C:\\Users\\Administrator\\Desktop\\blog\\github\\AILearners\\data\\ml\\jqxxsz\\9.RegTrees\\ex2test.txt'
    test_Data = loadDataSet(test_filename)
    test_Mat = np.mat(test_Data)
    print(prune(tree, test_Mat))

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   modelTree.py
@Time    :   2019/08/12 14:47:06
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   None
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

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
@description: 绘制ex00.txt数据集
@paramL filename - 文件名
@return: None
'''
def plotDataSet(filename):
    dataMat = loadDataSet(filename)                                        #加载数据集
    n = len(dataMat)                                                    #数据个数
    xcord = []; ycord = []                                                #样本点
    for i in range(n):                                                    
        xcord.append(dataMat[i][0]); ycord.append(dataMat[i][1])        #样本点
    fig = plt.figure()
    ax = fig.add_subplot(111)                                            #添加subplot
    ax.scatter(xcord, ycord, s = 20, c = 'blue',alpha = .5)                #绘制样本点
    plt.title('DataSet')                                                #绘制title
    plt.xlabel('X')
    plt.show()

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
@param:  dataSet - 数据集合
        leafType - 生成叶结点
        regErr - 误差估计函数
        ops - 用户定义的参数构成的元组
@return:  bestIndex - 最佳切分特征
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
    m, n = shape(dataSet)
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
@description: 绘制ex0.txt数据集
@paramL filename - 文件名
@return: None
'''
def plotDataSet1(filename):
    dataMat = loadDataSet(filename)                                        #加载数据集
    n = len(dataMat)                                                    #数据个数
    xcord = []; ycord = []                                                #样本点
    for i in range(n):                                                    
        xcord.append(dataMat[i][1]); ycord.append(dataMat[i][2])        #样本点
    fig = plt.figure()
    ax = fig.add_subplot(111)                                            #添加subplot
    ax.scatter(xcord, ycord, s = 20, c = 'blue',alpha = .5)                #绘制样本点
    plt.title('DataSet')                                                #绘制title
    plt.xlabel('X')
    plt.show()

# 回归树测试案例
# 为了和 modelTreeEval() 保持一致，保留两个输入参数
def regTreeEval(model, inDat):
    """
    Desc:
        对 回归树 进行预测
    Args:
        model -- 指定模型，可选值为 回归树模型 或者 模型树模型，这里为回归树
        inDat -- 输入的测试数据
    Returns:
        float(model) -- 将输入的模型数据转换为 浮点数 返回
    """
    return float(model)

def modelLeaf(dataSet):
    """
    Desc:
        当数据不再需要切分的时候，生成叶节点的模型。
    Args:
        dataSet -- 输入数据集
    Returns:
        调用 linearSolve 函数，返回得到的 回归系数ws
    """
    ws, X, Y = linearSolve(dataSet)
    return ws


# 计算线性模型的误差值
def modelErr(dataSet):
    """
    Desc:
        在给定数据集上计算误差。
    Args:
        dataSet -- 输入数据集
    Returns:
        调用 linearSolve 函数，返回 yHat 和 Y 之间的平方误差。
    """
    ws, X, Y = linearSolve(dataSet)
    yHat = X * ws
    # print corrcoef(yHat, Y, rowvar=0)
    return sum(power(Y - yHat, 2))


 # helper function used in two places
def linearSolve(dataSet):
    """
    Desc:
        将数据集格式化成目标变量Y和自变量X，执行简单的线性回归，得到ws
    Args:
        dataSet -- 输入数据
    Returns:
        ws -- 执行线性回归的回归系数 
        X -- 格式化自变量X
        Y -- 格式化目标变量Y
    """
    m, n = shape(dataSet)
    # 产生一个关于1的矩阵
    X = mat(ones((m, n)))
    Y = mat(ones((m, 1)))
    # X的0列为1，常数项，用于计算平衡误差
    X[:, 1: n] = dataSet[:, 0: n-1]
    Y = dataSet[:, -1]

    # 转置矩阵*矩阵
    xTx = X.T * X
    # 如果矩阵的逆不存在，会造成程序异常
    if linalg.det(xTx) == 0.0:
        raise NameError('This matrix is singular, cannot do inverse,\ntry increasing the second value of ops')
    # 最小二乘法求最优解:  w0*1+w1*x1=y
    ws = xTx.I * (X.T * Y)
    return ws, X, Y

# 预测结果
def createForeCast(tree, testData, modelEval=regTreeEval):
    """
    Desc:
        调用 treeForeCast ，对特定模型的树进行预测，可以是 回归树 也可以是 模型树
    Args:
        tree -- 已经训练好的树的模型
        testData -- 输入的测试数据
        modelEval -- 预测的树的模型类型，可选值为 regTreeEval（回归树） 或 modelTreeEval（模型树），默认为回归树
    Returns:
        返回预测值矩阵
    """
    m = len(testData)
    yHat = mat(zeros((m, 1)))
    # print yHat
    for i in range(m):
        yHat[i, 0] = treeForeCast(tree, mat(testData[i]), modelEval)
        # print "yHat==>", yHat[i, 0]
    return yHat




# 模型树测试案例
# 对输入数据进行格式化处理，在原数据矩阵上增加第0列，元素的值都是1，
# 也就是增加偏移值，和我们之前的简单线性回归是一个套路，增加一个偏移量
def modelTreeEval(model, inDat):
    """
    Desc:
        对 模型树 进行预测
    Args:
        model -- 输入模型，可选值为 回归树模型 或者 模型树模型，这里为模型树模型，实则为 回归系数
        inDat -- 输入的测试数据
    Returns:
        float(X * model) -- 将测试数据乘以 回归系数 得到一个预测值 ，转化为 浮点数 返回
    """
    n = shape(inDat)[1]
    X = mat(ones((1, n+1)))
    X[:, 1: n+1] = inDat
    # print X, model
    return float(X * model)

if __name__ == "__main__":
    # filename = 'C:\\Users\\Administrator\\Desktop\\blog\\github\\AILearners\\data\\ml\\jqxxsz\\9.RegTrees\\exp2.txt'
    # plotDataSet(filename)

    # 模型树
    myDat = loadDataSet('C:\\Users\\Administrator\\Desktop\\blog\\github\\AILearners\\data\\ml\\jqxxsz\\9.RegTrees\\exp2.txt')
    myMat = mat(myDat)
    myTree2 = createTree(myMat, modelLeaf, modelErr, ops=(1, 20))
    print(myTree2)
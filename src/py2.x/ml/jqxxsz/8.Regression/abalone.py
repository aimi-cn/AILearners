#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   abalone.py
@Time    :   2019/07/08 14:50:05
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   线性回归基础篇之预测鲍鱼年龄
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

'''
@description: 加载数据
@param : fileName - 文件名
@return:  xArr - x数据集
          yArr - y数据集
'''
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    xArr = []; yArr = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        xArr.append(lineArr)
        yArr.append(float(curLine[-1]))
    return xArr, yArr

'''
@description: 使用局部加权线性回归计算回归系数w
@param : testPoint - 测试样本点
        xArr - x数据集
        yArr - y数据集
        k - 高斯核的k,自定义参数
@return: testPoint * ws - 测试点*回归系数->预测结果
'''
def lwlr(testPoint, xArr, yArr, k = 1.0):
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    m = np.shape(xMat)[0]
    #创建权重对角矩阵
    weights = np.mat(np.eye((m)))
    #遍历数据集计算每个样本的权重
    for j in range(m):
        diffMat = testPoint - xMat[j, :]                                 
        weights[j, j] = np.exp(diffMat * diffMat.T/(-2.0 * k**2))
    xTx = xMat.T * (weights * xMat)                                        
    if np.linalg.det(xTx) == 0.0:
        print("矩阵为奇异矩阵,不能求逆").decode('utf-8').encode('gb2312')
        return
    #计算回归系数
    ws = xTx.I * (xMat.T * (weights * yMat))                            
    return testPoint * ws

'''
@description: 局部加权线性回归测试
@param : testArr - 测试数据集,测试集
        xArr - x数据集,训练集
        yArr - y数据集,训练集
        k - 高斯核的k,自定义参数
@return: ws - 回归系数
'''
def lwlrTest(testArr, xArr, yArr, k=1.0):
    #计算测试数据集大小
    m = np.shape(testArr)[0]                                           
    yHat = np.zeros(m)    
    #对每个样本点进行预测
    for i in range(m):                                                    
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat
'''
@description: 计算回归系数w
@param : xArr - x数据集
        yArr - y数据集
@return: ws - 回归系数
'''
def standRegres(xArr,yArr):
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    #根据文中推导的公示计算简答回归系数
    xTx = xMat.T * xMat                           
    if np.linalg.det(xTx) == 0.0:
        print("矩阵为奇异矩阵,不能求逆")
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws
'''
@description: 误差大小评测函数
@param : yArr - 真实数据
        yHatArr - 预测数据
@return: 误差大小
'''
def rssError(yArr, yHatArr):
    return ((yArr - yHatArr) **2).sum()

if __name__ == "__main__":
    abX, abY = loadDataSet('C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/8.Regression/abalone.txt')
    print('训练集与测试集相同:局部加权线性回归,核k的大小对预测的影响:')
    yHat01 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 0.1)
    yHat1 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 1)
    yHat10 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 10)
    print('k=0.1时,误差大小为:',rssError(abY[0:99], yHat01.T))
    print('k=1  时,误差大小为:',rssError(abY[0:99], yHat1.T))
    print('k=10 时,误差大小为:',rssError(abY[0:99], yHat10.T))
    print('')

    print('训练集与测试集不同:局部加权线性回归,核k的大小是越小越好吗？更换数据集,测试结果如下:')
    yHat01 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 0.1)
    yHat1 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 1)
    yHat10 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 10)
    print('k=0.1时,误差大小为:',rssError(abY[100:199], yHat01.T))
    print('k=1  时,误差大小为:',rssError(abY[100:199], yHat1.T))
    print('k=10 时,误差大小为:',rssError(abY[100:199], yHat10.T))
    print('')

    print(u"训练集与测试集不同:简单的线性归回与k=1时的局部加权线性回归对比:")
    print(u"k=1时,误差大小为:", rssError(abY[100:199], yHat1.T))
    ws = standRegres(abX[0:99], abY[0:99])
    yHat = np.mat(abX[100:199]) * ws
    print(u'简单的线性回归误差大小:', rssError(abY[100:199], yHat.T.A))
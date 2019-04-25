#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   KNN_demo03.py
@Time    :   2019/04/25 10:24:54
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   机器学习实战 2.3 k-近邻算法例子-sklearn手写数字识别
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
import numpy as np
import operator
from os import listdir
from sklearn.neighbors import KNeighborsClassifier as kNN

def img2vector(filename):
    """
    将图像数据转换为向量
    :param filename: 图片文件 因为我们的输入数据的图片格式是 32 * 32的
    :return: 一维矩阵
    该函数将图像转换为向量：该函数创建 1 * 1024 的NumPy数组，然后打开给定的文件，
    循环读出文件的前32行，并将每行的头32个字符值存储在NumPy数组中，最后返回数组。
    大致流程简单解释：第一个i 每次循环一次读取一行 第一个j把第一行的i值赋值到对应的数组位置里面 eg：i=0时 lineStr=“00000000000001111000000000000000”
    returnVector[0, 32*0 + 0] = int(lineStr[0])  returnVector[0, 32*0 + 1] = int(lineStr[1]) 一直循环32次 然后i=1 继续下去
    """
    #创建1x1024零向量
    returnVector = np.zeros((1,1024))
    #打开文件
    fr = open(filename)
    #安行读取
    for i in range(32):
        #第一行数据
        lineStr = fr.readline()
        #每一行的前32个元素依次添加到returnVect中
        for j in range(32):
            returnVector[0, 32*i+j] = int(lineStr[j])
    #返回转换后的1x1024向量
    return returnVector

'''
@description: 手写数字分类测试
@param {} 
@return: 
'''
def handwritingClassTest():
    #测试集的Labels
    hwLabels = []
    #返回trainingDigits目录下的文件名
    trainingFileList = listdir('data/2.KNN/trainingDigits')
    #返回文件夹下文件的个数
    m = len(trainingFileList)
    #初始化训练的Mat矩阵,测试集
    trainingMat = np.zeros((m, 1024))
    #从文件名中解析出训练集的类别
    for i in range(m):
        #获得文件的名字
        fileNameStr = trainingFileList[i]
        #获得分类的数字
        classNumber = int(fileNameStr.split('_')[0])
        #将获得的类别添加到hwLabels中
        hwLabels.append(classNumber)
        #将每一个文件的1x1024数据存储到trainingMat矩阵中
        trainingMat[i,:] = img2vector('data/2.KNN/trainingDigits/%s' % (fileNameStr))
    #构建kNN分类器
    neigh = kNN(n_neighbors = 3, algorithm = 'auto')
    #拟合模型, trainingMat为测试矩阵,hwLabels为对应的标签
    neigh.fit(trainingMat, hwLabels)
    #返回testDigits目录下的文件列表
    testFileList = listdir('data/2.KNN/testDigits')
    #错误检测计数
    errorCount = 0.0
    #测试数据的数量
    mTest = len(testFileList)
    #从文件中解析出测试集的类别并进行分类测试
    for i in range(mTest):
        #获得文件的名字
        fileNameStr = testFileList[i]
        #获得分类的数字
        classNumber = int(fileNameStr.split('_')[0])
        #获得测试集的1x1024向量,用于训练
        vectorUnderTest = img2vector('data/2.KNN/testDigits/%s' % (fileNameStr))
        #获得预测结果
        # classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        classifierResult = neigh.predict(vectorUnderTest)
        print("分类返回结果为%d\t真实结果为%d" % (classifierResult, classNumber)).decode('utf-8').encode('gb2312')
        if(classifierResult != classNumber):
            errorCount += 1.0
    print("总共错了%d个数据\n错误率为%f%%" % (errorCount, errorCount/mTest * 100)).decode('utf-8').encode('gb2312')

if __name__ == '__main__':
    handwritingClassTest()
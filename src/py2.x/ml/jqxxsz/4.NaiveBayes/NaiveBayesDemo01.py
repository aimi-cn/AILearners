#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   NaiveBayesDemo01.py
@Time    :   2019/05/16 15:00:33
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   朴素贝叶斯案例：屏蔽社区留言板的侮辱性言论
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
import numpy as np
from numpy import *

'''
@description: 创建实验样本
@param {None} 
@return: postingList - 实验样本切分的词条
         classVec - 类别标签向量 0代表非侮辱类 1代表侮辱类
'''
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],                #切分的词条
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]                                                                   #类别标签向量，1代表侮辱性词汇，0代表不是
    return postingList,classVec

'''
@description: 将切分的实验样本词条整理成不重复的词条列表，也就是词汇表
@param dataSet - 整理的样本数据集
@return: vocabSet - 返回不重复的词条列表，也就是词汇表
'''   
def createVocabList(dataSet):
    vocabSet = set([])                      #创建一个空的不重复列表
    for document in dataSet:               
        vocabSet = vocabSet | set(document) #取并集
    return list(vocabSet)

'''
@description: 根据vocabList词汇表，将inputSet向量化，向量的每个元素为1或0 1存在 0不存在
@param: vocabList - createVocabList返回的列表
inputSet - 切分的词条列表
@return: returnVec - 文档向量,词集模型
'''
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)                                    #创建一个其中所含元素都为0的向量
    for word in inputSet:                                                #遍历每个词条
        if word in vocabList:                                            #如果词条存在于词汇表中，则置1
            returnVec[vocabList.index(word)] = 1
        else: print("the word: %s is not in my Vocabulary!" % word)
    return returnVec                                                    #返回文档向量

'''
@description: 朴素贝叶斯分类器训练函数
@param :
    trainMatrix - 训练文档矩阵，即setOfWords2Vec返回的returnVec构成的矩阵
    trainCategory - 训练类别标签向量，即loadDataSet返回的classVec
@return: 
    p0Vect - 非侮辱类的条件概率数组
    p1Vect - 侮辱类的条件概率数组
    pAbusive - 文档属于侮辱类的概率
'''
def trainNB0(trainMatrix,trainCategory):
     #计算训练的文档数目 本文中6个
    numTrainDocs = len(trainMatrix)  
    #计算每篇文档的词条数   32个  也就是不重复的词条数                    
    numWords = len(trainMatrix[0])  
    #文档属于侮辱类的概率   0.5  --->  (0+1+0+1+0+1)/6                 
    pAbusive = sum(trainCategory)/float(numTrainDocs)  
    #创建numpy.zeros数组,词条出现数初始化为0 表示每个词条出现的个数
    p0Num = np.zeros(numWords); p1Num = np.zeros(numWords)  
    #分母初始化为0  词条总数
    p0Denom = 0.0; p1Denom = 0.0                            
    for i in range(numTrainDocs):
        #统计属于侮辱类的条件概率所需的数据，即P(w0|1),P(w1|1),P(w2|1)···
        if trainCategory[i] == 1:                            
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else: 
            #统计属于非侮辱类的条件概率所需的数据，即P(w0|0),P(w1|0),P(w2|0)···                                               
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom                                      
    p0Vect = p0Num/p0Denom    
    #返回属于侮辱类的条件概率数组，属于非侮辱类的条件概率数组，文档属于侮辱类的概率     
    return p0Vect,p1Vect,pAbusive                            

def trainNB1(trainMatrix, trainCategory):
    """
    训练数据优化版本
    :param trainMatrix: 文件单词矩阵
    :param trainCategory: 文件对应的类别
    :return:
    """
    # 总文件数
    numTrainDocs = len(trainMatrix)
    # 总单词数
    numWords = len(trainMatrix[0])
    # 侮辱性文件的出现概率
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 构造单词出现次数列表
    # p0Num 正常的统计
    # p1Num 侮辱的统计
    p0Num = ones(numWords)#[0,0......]->[1,1,1,1,1.....]
    p1Num = ones(numWords)

    # 整个数据集单词出现总数，2.0根据样本/实际调查结果调整分母的值（2主要是避免分母为0，当然值可以调整）
    # p0Denom 正常的统计
    # p1Denom 侮辱的统计
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            # 累加辱骂词的频次
            p1Num += trainMatrix[i]
            # 对每篇文章的辱骂的频次 进行统计汇总
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # 类别1，即侮辱性文档的[log(P(F1|C1)),log(P(F2|C1)),log(P(F3|C1)),log(P(F4|C1)),log(P(F5|C1))....]列表
    p1Vect = log(p1Num / p1Denom)
    # 类别0，即正常文档的[log(P(F1|C0)),log(P(F2|C0)),log(P(F3|C0)),log(P(F4|C0)),log(P(F5|C0))....]列表
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

'''
@description: 
@param:
    vec2Classify - 待测数据[0,1,1,1,1...]，即要分类的向量
    p0Vect - 非侮辱类的条件概率数组
    p1Vect - 侮辱类的条件概率数组
    pAbusive - 文档属于侮辱类的概率
@return: 
类别1是侮辱类 or 0不是

'''
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    # 将乘法转换为加法 使用优化算法 之前的乘法换成log之后直接用加法就可以
    #乘法：P(C|F1F2...Fn) = P(F1F2...Fn|C)P(C)/P(F1F2...Fn)
    #加法：P(F1|C)*P(F2|C)....P(Fn|C)P(C) -> log(P(F1|C))+log(P(F2|C))+....+log(P(Fn|C))+log(P(C))
    # p1 = reduce(lambda x,y:x*y, vec2Classify * p1Vec) * pClass1                #对应元素相乘
    # p0 = reduce(lambda x,y:x*y, vec2Classify * p0Vec) * (1.0 - pClass1)
    p1 = sum(vec2Classify * p1Vec) + log(pClass1) # P(w|c1) * P(c1) ，即贝叶斯准则的分子
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1) # P(w|c0) * P(c0) ，即贝叶斯准则的分子·
    print('p0:',p0)
    print('p1:',p1)
    if p1 > p0:
        return 1
    else: 
        return 0

def testingNB():
    listOPosts,listClasses = loadDataSet()                                    #创建实验样本
    myVocabList = createVocabList(listOPosts)                                #创建词汇表
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))                #将实验样本向量化
    p0V,p1V,pAb = trainNB1(np.array(trainMat),np.array(listClasses))        #训练朴素贝叶斯分类器
    testEntry = ['love', 'my', 'dalmation']                                    #测试样本1
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))                #测试样本向量化
    if classifyNB(thisDoc,p0V,p1V,pAb):
        print(testEntry)                                    #执行分类并打印分类结果
        print('属于侮辱类').decode('utf-8').encode('gb2312')
    else:
        print(testEntry)                                        #执行分类并打印分类结果
        print('属于非侮辱类').decode('utf-8').encode('gb2312')
    testEntry = ['stupid', 'garbage']                                        #测试样本2
 
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))                #测试样本向量化
    if classifyNB(thisDoc,p0V,p1V,pAb):
        print(testEntry)                                        #执行分类并打印分类结果
        print('属于侮辱类').decode('utf-8').encode('gb2312')
    else:
        print(testEntry)
        print('属于非侮辱类').decode('utf-8').encode('gb2312')   

if __name__ == '__main__':
    # postingLIst, classVec = loadDataSet()
    # for each in postingLIst:
    #     print(each)
    # print(classVec)
    
    # postingList, classVec = loadDataSet()
    # print('postingList:\n',postingList)
    # myVocabList = createVocabList(postingList)
    # print('myVocabList:\n',myVocabList)
    # trainMat = []
    # for postinDoc in postingList:
    #     trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    # print('trainMat:\n', trainMat)

    # postingList, classVec = loadDataSet()
    # myVocabList = createVocabList(postingList)
    # print('myVocabList:\n', myVocabList)
    # trainMat = []
    # for postinDoc in postingList:
    #     trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    # p0V, p1V, pAb = trainNB0(trainMat, classVec)
    # print('p0V:\n', p0V)
    # print('p1V:\n', p1V)
    # print('classVec:\n', classVec)
    # print('pAb:\n', pAb)

    testingNB()



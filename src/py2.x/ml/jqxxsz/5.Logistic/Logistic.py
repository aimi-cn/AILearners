#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Logistic.py
@Time    :   2019/05/21 20:36:26
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   逻辑回归
@github  :   https://github.com/aimi-cn/AILearners
'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

'''
@description: 梯度上升算法测试函数
求函数f(x) = -x^2 + 4x的极大值
@param {type} 
@return: 
'''
def Gradient_Ascent_test():
    #f(x)的导数
    def f_prime(x_old):                                   
        return -2 * x_old + 4
    #初始值，给一个小于x_new的值
    x_old = -1    
    #梯度上升算法初始值，即从(0,0)开始                                        
    x_new = 0   
    #步长，也就是学习速率，控制更新的幅度                                        
    alpha = 0.01         
    #精度，也就是更新阈值                               
    presision = 0.00000001       
    #上面提到的公式                        
    while abs(x_new - x_old) > presision:
        x_old = x_new
        x_new = x_old + alpha * f_prime(x_old)  
    #打印最终求解的极值近似值         
    print(x_new)                                        


'''
@description: 加载数据
@param {type} 
@return: 
    dataMat - 数据列表
    labelMat - 标签列表
'''
def loadDataSet():
    #创建数据标签
    dataMat = []
    #创建标签列表
    labelMat = []
    #打开文件 
    fr = open('C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/5.Logistic/testSet.txt') 
    #逐行读取
    for line in fr.readlines():
        #去回车，放入列表
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    fr.close()
    return dataMat,labelMat

'''
@description: 绘制数据集
@param {type} 
@return: 
'''
def plotDataSet():
    #加载数据集
    dataMat, labelMat = loadDataSet()  
    #转换成numpy的array数组
    dataArr = np.array(dataMat)
    #数据个数n
    n = np.shape(dataMat)[0]
    #正样本
    xcord1 = []; ycord1 = []
    #负样本
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            #1为正样本
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])  
        else:
            #0为负样本
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])    
    fig = plt.figure()
    ax = fig.add_subplot(111)                                            #添加subplot
    ax.scatter(xcord1, ycord1, s = 20, c = 'red', marker = 's',alpha=.5)#绘制正样本
    ax.scatter(xcord2, ycord2, s = 20, c = 'green',alpha=.5)            #绘制负样本
    plt.title('DataSet')                                                #绘制title
    plt.xlabel('x'); plt.ylabel('y')                                    #绘制label
    plt.show()                     

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
    return weights.getA()                                              

def plotBestFit(weights):
    #加载数据集
    dataMat, labelMat = loadDataSet()   
    #转换成numpy的array数组 
    dataArr = np.array(dataMat)                                            
    #数据个数
    n = np.shape(dataMat)[0]                                            
    #正样本
    xcord1 = []; ycord1 = []                                            
    #负样本
    xcord2 = []; ycord2 = []                                            
    #根据数据集标签进行分类
    for i in range(n):                                                    
        if int(labelMat[i]) == 1:
            #1为正样本
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])    
        else:
            #0为正样本
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])    
    fig = plt.figure()
    #添加subplot
    ax = fig.add_subplot(111)   
    #绘制正样本                                        
    ax.scatter(xcord1, ycord1, s = 20, c = 'red', marker = 's',alpha=.5)
    #绘制负样本
    ax.scatter(xcord2, ycord2, s = 20, c = 'green',alpha=.5)            
    x = np.arange(-3.0, 3.0, 0.1)
    '''
    y怎么来的
    首先理论上是这个样子的。
    dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
    w0*x0+w1*x1+w2*x2=f(x)
    x0最开始就设置为1叻， x1 是x的值 x2就是我们画图的y值，而f(x)被我们磨合误差给算到w0,w1,w2身上去了
    z=0 是因为sigmoid函数为0 当sigmoid函数输入为0的时候 正好是两个分类（类别1和类别0）的分界线
    所以： w0+w1*x+w2*y=0 => y = (-w0-w1*x)/w2
    '''
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    #title
    plt.title('BestFit')    
    #label                                            
    plt.xlabel('X1'); plt.ylabel('X2')                                    
    plt.show()       

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

def stocGradAscent2(dataMatrix, classLabels, numIter=150):
    m,n = np.shape(dataMatrix)                                                #返回dataMatrix的大小。m为行数,n为列数。
    weights = np.ones(n)                                                       #参数初始化
    weights_array = np.array([])                                            #存储每次更新的回归系数
    for j in range(numIter):                                           
        dataIndex = list(range(m))
        for i in range(m):           
            alpha = 4/(1.0+j+i)+0.01                                            #降低alpha的大小，每次减小1/(j+i)。
            randIndex = int(np.random.uniform(0,len(dataIndex)))                #随机选取样本
            h = sigmoid(sum(dataMatrix[randIndex]*weights))                    #选择随机选取的一个样本，计算h
            error = classLabels[randIndex] - h                                 #计算误差
            weights = weights + alpha * error * dataMatrix[randIndex]       #更新回归系数
            weights_array = np.append(weights_array,weights,axis=0)         #添加回归系数到数组中
            del(dataIndex[randIndex])                                         #删除已经使用的样本
    weights_array = weights_array.reshape(numIter*m,n)                         #改变维度
    return weights,weights_array                                             #返回

def gradAscent2(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)                                        #转换成numpy的mat
    labelMat = np.mat(classLabels).transpose()                            #转换成numpy的mat,并进行转置
    m, n = np.shape(dataMatrix)                                            #返回dataMatrix的大小。m为行数,n为列数。
    alpha = 0.01                                                        #移动步长,也就是学习速率,控制更新的幅度。
    maxCycles = 500                                                        #最大迭代次数
    weights = np.ones((n,1))
    weights_array = np.array([])
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)                                #梯度上升矢量化公式
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
        weights_array = np.append(weights_array,weights)
    weights_array = weights_array.reshape(maxCycles,n)
    return weights.getA(),weights_array                                    #将矩阵转换为数组，并返回


def plotWeights(weights_array1,weights_array2):
    #设置汉字格式
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    #将fig画布分隔成1行1列,不共享x轴和y轴,fig画布的大小为(13,8)
    #当nrow=3,nclos=2时,代表fig画布被分为六个区域,axs[0][0]表示第一行第一列
    fig, axs = plt.subplots(nrows=3, ncols=2,sharex=False, sharey=False, figsize=(20,10))
    x1 = np.arange(0, len(weights_array1), 1)
    #绘制w0与迭代次数的关系
    axs[0][0].plot(x1,weights_array1[:,0])
    axs0_title_text = axs[0][0].set_title(u'梯度上升算法：回归系数与迭代次数关系',FontProperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel(u'W0',FontProperties=font)
    plt.setp(axs0_title_text, size=20, weight='bold', color='black') 
    plt.setp(axs0_ylabel_text, size=20, weight='bold', color='black')
    #绘制w1与迭代次数的关系
    axs[1][0].plot(x1,weights_array1[:,1])
    axs1_ylabel_text = axs[1][0].set_ylabel(u'W1',FontProperties=font)
    plt.setp(axs1_ylabel_text, size=20, weight='bold', color='black')
    #绘制w2与迭代次数的关系
    axs[2][0].plot(x1,weights_array1[:,2])
    axs2_xlabel_text = axs[2][0].set_xlabel(u'迭代次数',FontProperties=font)
    axs2_ylabel_text = axs[2][0].set_ylabel(u'W2',FontProperties=font)
    plt.setp(axs2_xlabel_text, size=20, weight='bold', color='black') 
    plt.setp(axs2_ylabel_text, size=20, weight='bold', color='black')


    x2 = np.arange(0, len(weights_array2), 1)
    #绘制w0与迭代次数的关系
    axs[0][1].plot(x2,weights_array2[:,0])
    axs0_title_text = axs[0][1].set_title(u'改进的随机梯度上升算法：回归系数与迭代次数关系',FontProperties=font)
    axs0_ylabel_text = axs[0][1].set_ylabel(u'W0',FontProperties=font)
    plt.setp(axs0_title_text, size=20, weight='bold', color='black') 
    plt.setp(axs0_ylabel_text, size=20, weight='bold', color='black')
    #绘制w1与迭代次数的关系
    axs[1][1].plot(x2,weights_array2[:,1])
    axs1_ylabel_text = axs[1][1].set_ylabel(u'W1',FontProperties=font)
    plt.setp(axs1_ylabel_text, size=20, weight='bold', color='black')
    #绘制w2与迭代次数的关系
    axs[2][1].plot(x2,weights_array2[:,2])
    axs2_xlabel_text = axs[2][1].set_xlabel(u'迭代次数',FontProperties=font)
    axs2_ylabel_text = axs[2][1].set_ylabel(u'W2',FontProperties=font)
    plt.setp(axs2_xlabel_text, size=20, weight='bold', color='black') 
    plt.setp(axs2_ylabel_text, size=20, weight='bold', color='black')

    plt.show() 

if __name__ == '__main__':
    # Gradient_Ascent_test()

    # plotDataSet()

    # dataMat, labelMat = loadDataSet()           
    # print(gradAscent(dataMat, labelMat))
    
    # dataMat, labelMat = loadDataSet()           
    # weights = gradAscent(dataMat, labelMat)
    # plotBestFit(weights)

    # dataMat, labelMat = loadDataSet()
    # weights = stocGradAscent1(np.array(dataMat), labelMat)
    # plotBestFit(weights)

    ## 回归系数与迭代次数的关系
    dataMat, labelMat = loadDataSet()           
    weights1,weights_array1 = gradAscent2(dataMat, labelMat)

    weights2,weights_array2 = stocGradAscent2(np.array(dataMat), labelMat)
    plotWeights(weights_array1, weights_array2)
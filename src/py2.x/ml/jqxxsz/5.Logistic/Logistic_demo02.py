#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Logistic_demo02.py
@Time    :   2019/05/28 15:48:44
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   Logistic回归案例之预测病马死亡率 Sklearn实现
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
from sklearn.linear_model import LogisticRegression

def colicTest():
    frTrain = open('C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/5.Logistic/horseColicTraining.txt')                                        #打开训练集
    frTest = open('C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/5.Logistic/horseColicTest.txt')                                                #打开测试集
    trainingSet = []; trainingLabels = []
    testSet = []; testLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[-1]))
    for line in frTest.readlines():
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(len(currLine)-1):
            lineArr.append(float(currLine[i]))
        testSet.append(lineArr)
        testLabels.append(float(currLine[-1]))
    # 使用solver优化算法选择参数，只有五个可选参数 我们使用liblinear和sag进行优化
    # max_iter：算法收敛最大迭代次数，int类型，默认为10
    # classifier = LogisticRegression(solver='liblinear',max_iter=10).fit(trainingSet, trainingLabels)
    classifier = LogisticRegression(solver='sag',max_iter=3000).fit(trainingSet, trainingLabels)
    # score方法返回测试之后的正确率
    test_accurcy = classifier.score(testSet, testLabels) * 100
    print("正确率为: %.2f%%" % test_accurcy).decode('utf-8').encode('gb2312')

if __name__ == "__main__":
    colicTest()
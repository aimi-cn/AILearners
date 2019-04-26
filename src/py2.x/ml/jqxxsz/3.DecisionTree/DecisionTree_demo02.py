#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DecisionTree_demo02.py
@Time    :   2019/04/18 11:20:30
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   决策树案例02预测隐形眼镜类型
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
import DecisionTree_demo01
import decisionTreePlot
if __name__ == '__main__':
    fr = open('C:/Users/Administrator/Desktop/blog/github/AILearners/data/sourceData/Ch03/lenses.txt')
    #解析tab键分隔的数据行
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    print(lenses)
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    myTree_lenses = DecisionTree_demo01.createTree(lenses, lensesLabels)
    decisionTreePlot.createPlot(myTree_lenses)
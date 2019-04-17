#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DecisionTree.py
@Time    :   2019/04/09 15:20:00
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   decisionTree
@github  :   https://github.com/xiaoming3526/ai-ming3526/
@reference:  https://github.com/apachecn/AiLearning/
'''

# here put the import lib
from __future__ import print_function
print(__doc__)
import operator
from math import log
from collections import Counter
import decisionTreePlot as dtPlot

'''
ctrl+alt+t
@description: 创建数据集
@param {None} 
@return: 返回数据集和对应的label标签
'''
def creatDataSet():
    '''
    |不浮出水面可以生存| 是否有脚蹼 |属于鱼类
    |1-是----------------------|-是------------|是
    |2-是---------------------  |-是------------|是
    |3-是---------------------  |-否------------|否
    |4-否---------------------  |-是------------|否
    |5-否---------------------  |-是------------|否
    '''
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

'''
@description: 计算给定数据集的香农熵
@param {type} 数据集
@return: 返回 每一组feature下的某个分类下，香农熵的信息期望
'''
def calcShannonEnt(dataSet):
    # -----------计算香农熵的第一种实现方式start--------------------------------------------------------------------------------
    #
    # numEntries = len(dataSet)
    # labelsCounts = {}
    # for featVec in dataSet:
    #     currentLabel = featVec[-1]
    #     if currentLabel not in labelsCounts.keys():
    #         labelsCounts[currentLabel] = 0
    #     labelsCounts[currentLabel] += 1
    # shannonEnt = 0.0
    # for key in labelsCounts:
    #     prob = float(labelsCounts[key])/numEntries
    #     shannonEnt -= prob * log(prob, 2)
    # -----------计算香农熵的第一种实现方式end--------------------------------------------------------------------------------

    # # -----------计算香农熵的第二种实现方式start--------------------------------------------------------------------------------
    # # 统计标签出现的次数
    #eg:Counter({'no': 3, 'yes': 2})
    label_count = Counter(data[-1] for data in dataSet)
    # # 计算概率
    probs = [float(p[1]) / len(dataSet) for p in label_count.items()]
    # # 计算香农熵
    shannonEnt = sum([-p * log(p, 2) for p in probs])
    # -----------计算香农熵的第二种实现方式end--------------------------------------------------------------------------------
    return shannonEnt

'''
@description: 按照给定特征划分数据集
@param {dataSet 数据集 : 待划分的数据集 
        index 表示每一行的index列 :划分数据集的特征
        value 表示index列对应的value值 :需要返回的特征的值
} 
@return: index列为value的数据集【该数据集需要排除index列】
demo:dataSet=[[1, 1, 'yes'],
      [1, 1, 'yes'],
      [1, 0, 'no'],
      [0, 1, 'no'],
      [0, 1, 'no']]
      splitDataSet(dataSet,0,1)
      这个方法代表的意思就是在上面的数据集中找到第0列值是1的数据 返回出来 并且返回值中不包含第0列的值
      现在可以看到第0列值为1的数据有[1, 1, 'yes']，[1, 1, 'yes']，[1, 0, 'no']三个，然后去掉第0列的值返回出来的就是[1, 'yes'], [1, 'yes'], [0, 'no']
'''
def splitDataSet(dataSet, index, value):
    # -----------划分数据集的第一种方式 start------------------------------------
    retDataSet = []
    for featVec in dataSet:
        # index列为value的数据集【该数据集需要排除index列】
        # 判断index列的值是否为value
        if featVec[index] == value:
            # [:index]表示前index行，即若 index 为2，就是取 featVec 的前 index 行
            reduceFeatVec = featVec[:index]
            # [index+1:]表示从跳过 index 的 index+1行，取接下来的数据
            # 收集结果值 index列为value的行【该行需要排除index列】
            '''
            对于extend append
            list.append(object) 向列表中添加一个对象object
            list.extend(sequence) 把一个序列seq的内容添加到列表中
            1、使用append的时候，是将new_media看作一个对象，整体打包添加到music_media对象中。
            2、使用extend的时候，是将new_media看作一个序列，将这个序列和music_media序列合并，并放在其后面。
            result = []
            result.extend([1,2,3])
            print result
            result.append([4,5,6])
            print result
            result.extend([7,8,9])
            print result
            结果：
            [1, 2, 3]
            [1, 2, 3, [4, 5, 6]]
            [1, 2, 3, [4, 5, 6], 7, 8, 9]
            '''
            reduceFeatVec.extend(featVec[index+1:])
            retDataSet.append(reduceFeatVec)
    # -----------划分数据集的第一种方式 end------------------------------------
    # -----------划分数据集的第二种方式 start------------------------------------
    #retDataSet = [data for data in dataSet for i,v in enumerate(data) if i == index and v == value]
    #这个没有排除第index列
    return retDataSet
    
'''
@description: 选择最好的数据集划分方式
@param {dataSet:数据集} 
@return: bestFeature ：最优的特征列
demo:可以看出infoGain信息增益0的时候是比较大的 所以最好的特征是0
输出：infoGain= 0.419973094022 bestFeature= 0 0.970950594455 0.550977500433
    infoGain= 0.170950594455 bestFeature= 1 0.970950594455 0.8
    0
'''
def chooseBestFeatureToSplit(dataSet):
    # -----------选择最优特征的第一种方式 start------------------------------------
    #先求第一行有多少特征 最后一行是label标签所以减去1
    numFeatures = len(dataSet[0]) - 1
    #Label标签信息熵
    baseEntropy = calcShannonEnt(dataSet)
    # 最优的信息增益值, 和最优的Featurn编号
    bestInfoGain, bestFeature = 0.0, -1
    for i in range(numFeatures):
        # 获取每一个实例的第i+1个feature，组成list集合
        #eg:[1, 1, 1, 0, 0] [1, 1, 0, 1, 1]
        featList = [example[i] for example in dataSet]
        # 获取剔重后的集合，使用set对list数据进行去重
        #eg:set([0, 1]) set([0, 1])
        uniqueVals = set(featList)
        # 创建一个临时的信息熵
        newEntropy = 0.0
        # 遍历某一列的value集合，计算该列的信息熵 
        # 遍历当前特征中的所有唯一属性值，对每个唯一属性值划分一次数据集，计算数据集的新熵值，并对所有唯一特征值得到的熵求和。
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            #计算这个subDataSet占整个dataSet的概率是多少
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        # gain[信息增益]: 划分数据集前后的信息变化， 获取信息熵最大的值
        # 信息增益是熵的减少或者是数据无序度的减少。最后，比较所有特征中的信息增益，返回最好特征划分的索引值。
        infoGain = baseEntropy - newEntropy
        #print('infoGain=', infoGain, 'bestFeature=', i, baseEntropy, newEntropy)
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    # -----------选择最优特征的第一种方式 end------------------------------------
    # # -----------选择最优特征的第二种方式 start------------------------------------
    # # 计算初始香农熵
    # base_entropy = calcShannonEnt(dataSet)
    # best_info_gain = 0
    # best_feature = -1
    # # 遍历每一个特征
    # for i in range(len(dataSet[0]) - 1):
    #     # 对当前特征进行统计
    #     feature_count = Counter([data[i] for data in dataSet])
    #     # 计算分割后的香农熵
    #     new_entropy = sum(feature[1] / float(len(dataSet)) * calcShannonEnt(splitDataSet(dataSet, i, feature[0])) \
    #                    for feature in feature_count.items())
    #     # 更新值
    #     info_gain = base_entropy - new_entropy
    #     print('No. {0} feature info gain is {1:.3f}'.format(i, info_gain))
    #     if info_gain > best_info_gain:
    #         best_info_gain = info_gain
    #         best_feature = i
    # return best_feature
    # # -----------选择最优特征的第二种方式 end------------------------------------
    return bestFeature

'''
@description: 选择出现次数最多的一个结果
@param {classList label列的集合} 
@return: bestFeature 最优的特征列
'''
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    # 倒叙排列classCount得到一个字典集合，然后取出第一个就是结果（yes/no），即出现次数最多的结果
    #classCount.iteritems() 返回一个迭代器 方法在需要迭代结果的时候使用最适合，而且它的工作效率非常的高
    '''
    #key=operator.itemgetter(1) 按照数据集第一个域进行排序 eg：
    a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    b = sorted(a, key=operator.itemgetter(2))
    print(b)
    [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    按照第三列数字进行排序
    '''
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print("sortedClassCount:" + sortedClassCount)
    return sortedClassCount[0][0]

'''
@description: 创建树
@param {dataSet, labels 数据集 对应的标签} 
@return: 
'''
def createTree(dataSet, labels):
    #返回数据集中最后一列的值
    # eg classList:['yes', 'yes', 'no', 'no', 'no']
    classList = [example[-1] for example in dataSet]
    # 如果数据集的最后一列的第一个值出现的次数=整个集合的数量，也就说只有一个类别，就只直接返回结果就行
    # 第一个停止条件：所有的类标签完全相同，则直接返回该类标签。
    # count() 函数是统计括号中的值在list中出现的次数
    # eg: classList:['yes', 'yes'] classList.count(classList[0])== len(classList)=2直接返回'yes'
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 如果数据集只有1列，那么最初出现label次数最多的一类，作为结果
    # 第二个停止条件：使用完了所有特征，仍然不能将数据集划分成仅包含唯一类别的分组。
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    # 选择最优的列，得到最优列对应的label含义
    bestFeat = chooseBestFeatureToSplit(dataSet)
    # 获取label的名称
    bestFeatLabel = labels[bestFeat]
    # 初始化myTree
    myTree = {bestFeatLabel: {}}
    # 注：labels列表是可变对象，在PYTHON函数中作为参数时传址引用，能够被全局修改
    # 所以这行代码导致函数外的同名变量被删除了元素，造成例句无法执行，提示'no surfacing' is not in list
    del(labels[bestFeat])
    # 取出最优列，然后它的branch做分类
    featValues = [example[bestFeat] for example in dataSet]
    # 获取剔重后的集合，使用set对list数据进行去重
    uniqueVals = set(featValues)
    for value in uniqueVals:
        # 求出剩余的标签label
        subLabels = labels[:]
        # 遍历当前选择特征包含的所有属性值，在每个数据集划分上递归调用函数createTree()
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
        print('myTree', value, myTree)
    return myTree

def classify(inputTree, featLabels, testVec):
    """classify(给输入的节点，进行分类)
    Args:
        inputTree  决策树模型
        featLabels Feature标签对应的名称
        testVec    测试输入的数据
    Returns:
        classLabel 分类的结果值，需要映射label才能知道名称
    """
    # 获取tree的根节点对于的key值
    firstStr = inputTree.keys()[0]
    # 通过key得到根节点对应的value
    secondDict = inputTree[firstStr]
    # 判断根节点名称获取根节点在label中的先后顺序，这样就知道输入的testVec怎么开始对照树来做分类
    featIndex = featLabels.index(firstStr)
    # 测试数据，找到根节点对应的label位置，也就知道从输入的数据的第几位来开始分类
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    print('+++', firstStr, 'xxx', secondDict, '---', key, '>>>', valueOfFeat)
    # 判断分枝是否结束: 判断valueOfFeat是否是dict类型
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel

def get_tree_height(tree):
    """
     Desc:
        递归获得决策树的高度
    Args:
        tree
    Returns:
        树高
    """

    if not isinstance(tree, dict):
        return 1

    child_trees = tree.values()[0].values()

    # 遍历子树, 获得子树的最大高度
    max_height = 0
    for child_tree in child_trees:
        child_tree_height = get_tree_height(child_tree)

        if child_tree_height > max_height:
            max_height = child_tree_height

    return max_height + 1


def fishTest():
    myData,labels = creatDataSet()

    #求数据集的香农熵
    # print(calcShannonEnt(myData))

    # # 求第0列 为 1/0的列的数据集【排除第0列】
    #print (splitDataSet(myData, 0, 1))
    #print (splitDataSet(myData, 0, 0))

    # bestFeature = chooseBestFeatureToSplit(myData)
    # print(bestFeature)
    import copy
    myTree = createTree(myData, copy.deepcopy(labels))
    #print(myTree)
    # [1, 1]表示要取的分支上的节点位置，对应的结果值
    # print(classify(myTree, labels, [1, 1]))
    
    # # 获得树的高度
    # print(get_tree_height(myTree))

    # # 画图可视化展现
    dtPlot.createPlot(myTree)

if __name__ == '__main__':
    fishTest()
    
    
    
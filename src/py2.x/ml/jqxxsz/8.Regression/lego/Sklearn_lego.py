#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Sklearn_lego.py
@Time    :   2019/07/22 20:16:06
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   用sklearn实现下岭回归
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
# -*-coding:utf-8 -*-
import numpy as np
from bs4 import BeautifulSoup
import random

'''
@description: 从页面读取数据，生成retX和retY列表
@param: retX - 数据X
        retY - 数据Y
        inFile - HTML文件
        yr - 年份
        numPce - 乐高部件数目
        origPrc - 原价
@return: 
'''
def scrapePage(retX, retY, inFile, yr, numPce, origPrc):
    # 打开并读取HTML文件
    with open(inFile, encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html)
    i = 1
    # 根据HTML页面结构进行解析
    currentRow = soup.find_all('table', r = "%d" % i)
    while(len(currentRow) != 0):
        currentRow = soup.find_all('table', r = "%d" % i)
        title = currentRow[0].find_all('a')[1].text
        lwrTitle = title.lower()
        # 查找是否有全新标签
        if (lwrTitle.find('new') > -1) or (lwrTitle.find('nisb') > -1):
            newFlag = 1.0
        else:
            newFlag = 0.0
        # 查找是否已经标志出售，我们只收集已出售的数据
        soldUnicde = currentRow[0].find_all('td')[3].find_all('span')
        if len(soldUnicde) == 0:
            print("商品 #%d 没有出售" % i)
        else:
            # 解析页面获取当前价格
            soldPrice = currentRow[0].find_all('td')[4]
            priceStr = soldPrice.text
            priceStr = priceStr.replace('$','')
            priceStr = priceStr.replace(',','')
            if len(soldPrice) > 1:
                priceStr = priceStr.replace('Free shipping', '')
            sellingPrice = float(priceStr)
            # 去掉不完整的套装价格
            if  sellingPrice > origPrc * 0.5:
                print("%d\t%d\t%d\t%f\t%f" % (yr, numPce, newFlag, origPrc, sellingPrice))
                retX.append([yr, numPce, newFlag, origPrc])
                retY.append(sellingPrice)
        i += 1
        currentRow = soup.find_all('table', r = "%d" % i)


'''
@description: 依次读取六种乐高套装的数据，并生成数据矩阵
@param {type} 
@return: 
'''
def setDataCollect(retX, retY):
    scrapePage(retX, retY, 'C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/8.Regression/lego/lego8288.html', 2006, 800, 49.99)                #2006年的乐高8288,部件数目800,原价49.99
    scrapePage(retX, retY, 'C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/8.Regression/lego/lego10030.html', 2002, 3096, 269.99)                #2002年的乐高10030,部件数目3096,原价269.99
    scrapePage(retX, retY, 'C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/8.Regression/lego/lego10179.html', 2007, 5195, 499.99)                #2007年的乐高10179,部件数目5195,原价499.99
    scrapePage(retX, retY, 'C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/8.Regression/lego/lego10181.html', 2007, 3428, 199.99)                #2007年的乐高10181,部件数目3428,原价199.99
    scrapePage(retX, retY, 'C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/8.Regression/lego/lego10189.html', 2008, 5922, 299.99)                #2008年的乐高10189,部件数目5922,原价299.99
    scrapePage(retX, retY, 'C:/Users/Administrator/Desktop/blog/github/AILearners/data/ml/jqxxsz/8.Regression/lego/lego10196.html', 2009, 3263, 249.99)                #2009年的乐高10196,部件数目3263,原价249.99

'''
@description: 使用sklearn
@param {type} 
@return: 
'''
def usesklearn():
    from sklearn import linear_model
    reg = linear_model.Ridge(alpha = .5)
    lgX = []
    lgY = []
    setDataCollect(lgX, lgY)
    reg.fit(lgX, lgY)
    print('%f%+f*年份%+f*部件数量%+f*是否为全新%+f*原价' % (reg.intercept_, reg.coef_[0], reg.coef_[1], reg.coef_[2], reg.coef_[3]))    

if __name__ == '__main__':
    usesklearn()
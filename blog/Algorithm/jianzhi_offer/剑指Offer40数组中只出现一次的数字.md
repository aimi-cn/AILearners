# 剑指Offer（四十）：数组中只出现一次的数字

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击CSDN和github链接：  
[剑指Offer完整习题解析CSDN地址](https://blog.csdn.net/baidu_31657889/article/category/9059648)  
[github地址](https://github.com/aimi-cn/AILearners/tree/master/blog/Algorithm/jianzhi_offer)

## 二、题目

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

### 1、思路

简单的大家都可以想到的实现方法，做一个字典来存放遍历的数组，次数为1的就是我们要返回的值。

看代码~

### 2、编程实现

**python**

代码实现方案：

```python
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        s = {}
        for i in range(len(array)):
            if array[i] not in s:
                s[array[i]] = 1
            else:
                s[array[i]] += 1
        res = []
        for key,value in s.items():
            if value == 1:
                res.append(key)
        return res
```

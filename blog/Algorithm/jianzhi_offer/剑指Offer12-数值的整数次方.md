# 剑指Offer（十二）：数值的整数次方

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)

## 二、题目

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

### 1、思路

看到这个题，脑子里第一个想法是调用python库的同学请举手哈哈哈哈~pow(base,exponent)一行解决的事~python大发好啊！
关键是牛客网还给过了===

但是我们还是严谨的来看这道题把

当指数为负数的时候，可以先对指数求绝对值，然后算出次方的结果之后再取倒数。如果底数为0，则直接返回0。此时的次方在数学上是没有意义的。


### 2、编程实现

**python2.7**

代码实现方案：

```python
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        flag = 0
        result = 1
        if base == 0:
            return False
        if exponent < 0:
            flag = 1
        for i in range(abs(exponent)):
            result *= base
        if flag == 1:
            result = 1 / result
        return result
```
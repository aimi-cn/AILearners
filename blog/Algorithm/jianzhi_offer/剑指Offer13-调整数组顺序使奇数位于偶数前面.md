# 剑指Offer（十三）：调整数组顺序使奇数位于偶数前面

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)

## 二、题目

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

### 1、思路

看到这个题 我们乍一看大部分人还是有想法的 无非是取出两个数组一个数组放前面的奇数一个数组放后面的偶数 然后拼接起来就是我们要的结果了。

也就是创建两个数组，遍历数组，奇数前插入第一个数组，偶数后插入第二个数组。最后将两个数组拼接起来。


### 2、编程实现

**python2.7**

代码实现方案：

```python
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        qian = [];hou = []
        for i in array:
            qian.append(i) if i%2==1 else hou.append(i)
            #qian.append(i) if i%2==1 else hou.append(i)
        return qian+hou
```

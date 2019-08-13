# 剑指Offer（九）：变态跳台阶

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)

## 二、题目

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

### 1、思路

我想说 很多东西都可以使用数学归纳法来解决滴~

这不来了一个身强力壮贼能跳的青蛙 我们来用归纳法解决它！

- 当n=1时，结果为1；
- 当n=2时，结果为2；
- 当n=3时，结果为4；
。。。。

以此类推，我们可以发现，跳法f(n)=2^(n-1)。

### 2、编程实现

**python2.7**

代码实现方法：

```python
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)
```









# 剑指Offer（二十）：包含min函数的栈

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)

## 二、题目

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。


### 1、思路

时间复杂度在1的情况下，我们就不能使用遍历栈的方法了，所以我们的思路是利用一个辅助栈来存放最小值~

栈  3，4，2，5，1
辅助栈 3，3，2，2，1
每入栈一次，就与辅助栈顶比较大小，如果小就入栈，如果大就入栈到当前的辅助栈顶
当出栈时，辅助栈也要出栈
这种做法可以保证辅助栈顶一定都当前栈的最小值~

### 2、编程实现

**python2.7**

代码实现方案：

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []
         
    def push(self, node):
        min = self.min()
        if not min or node < min:
            self.assist.append(node)
        else:
            self.assist.append(min)
        self.stack.append(node)
         
    def pop(self):
        if self.stack:
            self.assist.pop()
            return self.stack.pop()
        
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
         
    def min(self):
        # write code here
        if self.assist:
            return self.assist[-1]
```

# 剑指Offer（三）：从尾到头打印链表

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)

## 二、题目

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

### 1、思路

首先我想到的是既然是使用相反顺序来返回这个链表，是不是可以直接把这个链表遍历出来之后，直接使用python的倒序排列方法[::-1]来返回，不就是我们要的结果吗~
或者直接使用python的插入方法，遍历整个链表，每次插入数据，只插入在首位，这样返回出来的result也会是需要返回的结果。


### 2、编程实现

**python2.7**

第一种思路代码实现：
```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        if listNode is None:
            return result
        while listNode.next is not None:
            result.append(listNode.val)
            listNode = listNode.next
            
        result.extend([listNode.val])
        
        return result[::-1]
```

第二种思路代码实现：

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        result = []
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result
```









# 剑指Offer（三十六）：两个链表的第一个公共结点

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击CSDN和github链接：  
[剑指Offer完整习题解析CSDN地址](https://blog.csdn.net/baidu_31657889/article/category/9059648)  
[github地址](https://github.com/aimi-cn/AILearners/tree/master/blog/Algorithm/jianzhi_offer)

## 二、题目

输入两个链表，找出它们的第一个公共结点。

### 1、思路

如果存在共同节点的话，那么从该节点，两个链表之后的元素都是相同的。也就是说两个链表从尾部往前到某个点，节点都是一样的。

两条相交的链表呈Y型。可以从两条链表尾部同时出发，最后一个相同的结点就是链表的第一个相同的结点。可以利用栈来实现。时间复杂度有O(m + n), 空间复杂度为O(m + n)

### 2、编程实现

**python**

代码实现方案：


```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        
        #定义一个新的栈倒叙存放两个节点
        stack1 = []
        stack2 = []
        
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
            
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
            
        first = None
        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1 is top2:
                first=top1
            else:
                break
        return first
```

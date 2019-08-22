# 剑指Offer（十五）：反转链表

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)

## 二、题目

输入一个链表，反转链表后，输出新链表的表头。

### 1、思路

这个题对我来说还是有点难度了 其实原理不难 我们我们使用三个指针，分别指向当前遍历到的结点、它的前一个结点以及后一个结点。

在遍历的时候，做当前结点的尾结点和前一个结点的替换。

因为这个题目之前在刷LeetCode的时候已经做过详细的图解说明 大家看链接就可以：https://blog.csdn.net/baidu_31657889/article/details/91552141


### 2、编程实现

**python2.7**

代码实现方案：

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        pre = None
        while pHead:
            next = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = next
        return pre
```

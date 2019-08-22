# 剑指Offer（十六）：合并两个排序的链表

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)

## 二、题目

输入一个链表，反转链表后，输出新链表的表头。

### 1、思路

- 比较两个链表的首结点，哪个小的的结点则合并到第三个链表尾结点，并向前移动一个结点。
- 步骤一结果会有一个链表先遍历结束，或者没有
- 第三个链表尾结点指向剩余未遍历结束的链表
- 返回第三个链表首结点

详细过程见代码实现部分~~~


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
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        #先创建空的第三节点
        new_head = ListNode(0)
        #返回的是合并后的列表 所以让一个节点等于这个空的节点
        pHead = new_head
        #进行排序
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                new_head.next = pHead2
                pHead2 = pHead2.next
            else:
                new_head.next = pHead1
                pHead1 = pHead1.next
            new_head = new_head.next
        # 便利剩下没遍历的列表
        if pHead1:
            new_head.next = pHead1
        elif pHead2:
            new_head.next = pHead2
        return pHead.next
```

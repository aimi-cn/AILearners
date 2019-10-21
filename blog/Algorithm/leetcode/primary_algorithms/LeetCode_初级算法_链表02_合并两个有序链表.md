# LeetCode初级算法--链表02：合并两个有序链表

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> csdn：https://blog.csdn.net/abcgkj/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这是由LeetCode官方推出的的经典面试题目清单~  
这个模块对应的是探索的初级算法~旨在帮助入门算法。我们第一遍刷的是leetcode推荐的题目。  
查看完整的剑指Offer算法题解析请点击github链接：  
[github地址](https://github.com/aimi-cn/AILearners/tree/master/blog/Algorithm/leetcode/primary_algorithms)

## 二、题目

将两个有序链表合并为一个新的**有序链表**并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例:**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```


### 1、思路

首先我们看到的数一个有序的链表，所以我们可以先比较两个链表长度相等的部分，按照顺序进行排列，对于剩下一个链表的部分，直接插入到最终的链表中，详细过程见代码。

### 2、编程实现

**python**

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        #返回的是合并后的列表 所以让一个节点等于这个空的节点
        pHead = new_head
        #进行排序
        while l1 and l2:
            if l1.val > l2.val:
                new_head.next = l2
                l2 = l2.next
            else:
                new_head.next = l1
                l1 = l1.next
            new_head = new_head.next
        # 遍历剩下没遍历的列表
        if l1:
            new_head.next = l1
        elif l2:
            new_head.next = l2
        return pHead.next
```
# LeetCode初级算法--链表01：反转链表

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

反转一个单链表。

**示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

**进阶:**

你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


### 1、思路

这个题对我来说还是有点难度了，其实原理不难，我们我们使用三个指针，分别指向当前遍历到的结点、它的前一个结点以及后一个结点。

在遍历的时候，做当前结点的尾结点和前一个结点的替换。

因为这个题目之前在刷LeetCode的时候已经做过详细的图解说明 大家看链接就可以：https://blog.csdn.net/baidu_31657889/article/details/91552141

### 2、编程实现

**python**

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
```
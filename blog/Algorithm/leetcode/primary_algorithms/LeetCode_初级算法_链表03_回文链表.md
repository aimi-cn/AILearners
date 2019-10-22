# LeetCode初级算法--链表03：回文链表

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

请判断一个链表是否为回文链表。 

**示例1:**

```
输入: 1->2
输出: false
```

**示例2:**

```
输入: 1->2->2->1
输出: true
```

### 1、思路

- 使用一个数组来依次存储该链表中每个结点的数据。
- 判断该数组是否为回文数组。

### 2、编程实现

**python**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ls = []
        
        while head:
            ls.append(head.val)
            head = head.next
        
        n = len(ls)
        for i in range(n//2): # //表示取整
            if ls[i] != ls[n-i-1]:
                return False            
        return True
```

## 3、改进

很明显，上述方法时间和空间复杂度都为O(n)。但我们可以使用“快慢指针”来将空间复杂度降至O(1)。

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        # 快慢指针，快指针到达尾部，慢指针到达中间
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 奇数长，fast指针在最后一个，slow在最中间，slow需要往后过一个
        # 偶数长，fast为空，slow指针中点过一个
        if fast:
            slow = slow.next
        
        # 用于翻转链表后半部分
        # pre用于指向已经翻转的部分
        # cur指向还未翻转的部分
        pre = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True
```
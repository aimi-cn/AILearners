# LeetCode初级算法--链表04：环形链表

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

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

**示例1:**

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

![](../../../../img/Algorithm/LeetCode/LeetCode_初级算法_链表04_环形链表/circularlinkedlist.png)

**示例2:**

```
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

![](../../../../img/Algorithm/LeetCode/LeetCode_初级算法_链表04_环形链表/circularlinkedlist_test2.png)

**示例3:**

```
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```

![](../../../../img/Algorithm/LeetCode/LeetCode_初级算法_链表04_环形链表/circularlinkedlist_test3.png)

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

### 1、思路

和回文链表的思路一样，可以使用“快慢指针”。具体原理：

- 设置两指针fast和slow，初始状态都指向链表head。
- fast每轮走两步，slow每轮走一步。
- 若链表中存在环，fast和slow一定会在将来相遇。
- 若fast走到了链表尾部，则说明链表无环。

### 2、编程实现

**python**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
```
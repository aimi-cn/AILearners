# LeetCode初级算法--字符串02：字符串中的第一个唯一字符

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

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

```
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
```


### 1、思路

首先我们可以想到这道题需要的是一个不重复的字符，我们顺序找到第一个不重复的字符，把其索引存起来，返回最小的索引也就是第一个不重复的字符了。

注：使用count方法，会增加时间复杂度，所以我们用字典记录各字符的索引。如果重复出现，则索引值需要加上len(s)，小于len(s)的那个索引就是我们求的值。

### 2、编程实现

**python**

```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #算法超时
        # res = []
        # for i in s:
        #     if s.count(i) == 1:
        #         res.append(s.index(i))
        # if len(res):
        #     return min(res)
        # return -1
        
        # 用字典记录各字符的索引。如果重复出现，则索引值需要加上len(s)
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] += len(s)
        
        if len(s) and min(d.values()) < len(s) :
            return min(d.values())
        return -1
```
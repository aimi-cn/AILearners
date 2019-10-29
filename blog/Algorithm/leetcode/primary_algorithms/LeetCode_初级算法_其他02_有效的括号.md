# LeetCode初级算法--其他02：有效的括号

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

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

**示例1:**

```
输入: "()"
输出: true
```

**示例2:**

```
输入: "()[]{}"
输出: true
```

**示例3:**

```
输入: "(]"
输出: false
```

**示例4:**
```
输入: "([)]"
输出: false
```

**示例5:**
```
输入: "{[]}"
输出: true
```

### 1、思路

我们观察几个例子不难发现满足有效字符串的例子，对于正确的字符串来说，每次都能去掉一对括号，最后就成了空~

### 2、编程实现

**python**

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '[]' in s or '{}' in s or '()' in s:
            s = s.replace('[]','')
            s = s.replace('{}','')
            s = s.replace('()','')
        return s == ''
```
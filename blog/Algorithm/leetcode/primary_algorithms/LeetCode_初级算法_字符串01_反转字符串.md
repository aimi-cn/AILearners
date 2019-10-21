# LeetCode初级算法--字符串01：反转字符串

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

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1:

```
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
```

示例 2:

```
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```


### 1、思路

首先我们要注意是，不要给另外的数组分配额外的空间，你必须原地修改输入数组

python自带的reverse方法可以直接进行翻转，这是一种方法。

另一种方法，使用指针，我们可以看到翻转之后首位元素进行的调换，我们让头指针指向第一个元素，尾指针指向第二个元素，这样进行数组元素调换。

### 2、编程实现

**python**

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        #第一种使用reverse函数
        #s.reverse()
        
        #第二种使用指针
        head = 0
        tail = len(s)-1
        while head < tail:
            s[head],s[tail] = s[tail],s[head]
            head += 1
            tail -=1
```
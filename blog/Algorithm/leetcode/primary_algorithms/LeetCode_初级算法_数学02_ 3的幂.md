# LeetCode初级算法--数学02：3的幂

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

给定一个整数，写一个函数来判断它是否是 3 的幂次方。

**示例1:**

```
输入: 27
输出: true
```

**示例2:**

```
输入: 0
输出: false
```

**示例3:**

```
输入: 9
输出: true
```

**示例4:**

```
输入: 45
输出: false
```

进阶：
你能不使用循环或者递归来完成本题吗？

### 1、思路

该方法比较简单。这里只说两个需要注意的地方：
- 3的0次方是1，因此n==1是输出也为True。
- math.log 函数得到的数据可能不够精确，可以使用 round 取整。

### 2、编程实现

**python**

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** round(math.log(n, 3)) == n
```
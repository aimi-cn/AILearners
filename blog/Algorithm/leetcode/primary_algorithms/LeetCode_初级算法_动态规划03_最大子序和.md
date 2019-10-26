# LeetCode初级算法--动态规划03：最大子序和  

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

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**示例:**

```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

### 1、思路

该问题的目的是求最大子序和，我们可以将其转化为：求当前元素自身和包含之前元素后两者的较大值，并将较大值保存到nums中（避免再开辟新的空间来存储），最后返回nums里的最大值即可。

### 2、编程实现

**python**

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        for i in range(1, n):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        
        return max(nums)
```
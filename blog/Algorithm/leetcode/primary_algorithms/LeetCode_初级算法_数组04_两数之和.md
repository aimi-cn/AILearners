# LeetCode初级算法--数组04：两数之和

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

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例 1:

```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

注：该题有一个坑，题目说“你不能重复利用这个数组中同样的元素”。但是在测试时发现，有一个测试用例为:

```
nums=[3,3]，target=6，答案为 [0,1] 
```

所以说，题目中的意思应该是你虽然不能重复利用这个数组中同样的元素，但是你可以使用数组中值相同的元素。。。

### 1、思路

看到这种题目，我们先来暴力解法试试。

### 2、编程实现（Python3）

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) 
        for i in range(n):
            for j in range(i+1, n):
                if target-nums[i]==nums[j]:
                    return [i, j]
```

但时间复杂度达到了$O(n^2)$，因此我们需要改进一下。

### 3、改进

考虑是否可以只用一个for循环解决问题，将时间复杂度降至O(n)？由上一个题想到字典的key是唯一的，因此我们可以将元素设置为key，其索引设置为其对应的value。具体做法如下：

- 定义一个空字典。
- 遍历数组中的元素，n为目标值减去当前元素num。
- 如果n不是该字典的key，则将该元素num设为字典的key，并将该元素的索引设为其对应的value，方便我们返回结果。
- 如果n是该字典的key，很明显我们已经找到了答案。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
```
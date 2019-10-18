# LeetCode初级算法--数组03：两个数组的交集 II

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

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

```
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
```

示例 2:

```
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
```

说明：

- 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
- 我们可以不考虑输出结果的顺序。

### 1、思路

- 使用字典将第一个数组的所有元素和其对应的个数，分别转化为字典的key和value。
- 遍历第二个数组元素。如果该元素在字典中可以找到，且字典中的该元素个数大于0。则将该元素添加到最后返回的列表中，并使字典中该元素对应的个数减一。
- 返回结果。

### 2、编程实现（Python3）

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        counts = {}

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                # res.append(num)
                res += num,
                counts[num] -= 1

        return res
```

### 3、改进

我们可以使用Python中自带的collections包，对上述思路的第一步进行改进，是代码更加简化。具体做法如下：

```python
import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if num in counts and counts[num] > 0:
                # res.append(num)
                res += num,
                counts[num] -= 1
        return res
```

# LeetCode初级算法--设计问题01：Shuffle an Array （打乱数组）

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

打乱一个没有重复元素的数组。

**示例:**

```
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
```

### 1、思路

遍历数组每个位置，每次都随机生成一个坐标位置，然后交换当前位置和随机位置的数字，这样如果数组有n个数字，那么也随机交换了n组位置，从而达到了洗牌的目的。

### 2、编程实现

**python**

```python
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.data

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # 方法一：
        # ans = copy.deepcopy(self.data)
        # random.shuffle(ans)
        # return ans
        #方法二
        ans = copy.deepcopy(self.data)
        for i in range(len(ans)):
            j = random.randint(i, len(ans)-1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```
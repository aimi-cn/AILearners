# LeetCode初级算法--动态规划02：买卖股票的最佳时机  

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

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

**示例1:**

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```

**示例2:**

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

### 1、思路

对于本题，我们首先能想到的是暴力解法，如下所示：

### 2、编程实现

**python**

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
#         超出时间限制
        p_len = len(prices)    
        profit = 0
        
        for i in range(p_len):
            for j in range(i+1, p_len):
                temp = prices[j] - prices[i]
                if profit < temp:
                    profit = temp
        return profit
```

但很明显我们的时间复杂度达到了$O(n^2)$，并且超出时间限制。因此，我们需要进行改进。

### 3、改进

在这里，我们使用一次循环来解决该问题。较之暴力解法，我们添加一个min_pirce变量，用于存储最小购买值与当前值之间的较小值。**但是注意，我们取最大利润的时候，所使用的购买值并不一定是最小购买值**。例如对于序列“10 2 9 1”，我们去最大利润7时，使用的购买值为2（即9-2），并不是使用的最小购买值1，这与我们保存在min_price的值并不冲突。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            # 最大利润为当前值与最小购买值之差和max_profit的较大值
            max_profit=max(max_profit,price-min_price)
            # 最小购买值为当前值与min_price之间的较小值
            min_price=min(price,min_price)
        return max_profit
```
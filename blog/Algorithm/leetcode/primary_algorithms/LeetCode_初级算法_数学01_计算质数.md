# LeetCode初级算法--数学01：计算质数

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

统计所有小于非负整数 n 的质数的数量。

**示例:**

```
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
```

### 1、思路

按照惯例，我们第一时间想到的肯定是暴力解法。

### 2、编程实现

**python**

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            # for-else语句中，如果没有运行break，才会运行else里面的内容
            else:
                count += 1
        return count
```

果然，该暴力法超出时间限制了。。。

### 3、改进

在这里，我们用“厄拉多塞筛法”进行改进。该方法主要如下：

- 先将 2~n 的各个数放入表中。
- 从2开始，将2标为橙色，然后划去2的其他倍数；第一个既未画圈又没有被划去的数是3，并将其标为橙色，再划去3的其他倍数；
- 依次类推，直到根号n位置。这时，表中未被排除的就是我们所要求的质数。

![](../../../../img/Algorithm/LeetCode/LeetCode_初级算法_数学01_计算质数.md/100以内的质数筛选-埃式筛法.gif)

```python
class Solution:
    def countPrimes(self, n):
        
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # isPrime[i * i:n:i] = [0] * (len(isPrime[i * i:n:i]))
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)
```
# 剑指Offer（二十八）：数组中出现次数超过一半的数字

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击CSDN和github链接：  
[剑指Offer完整习题解析CSDN地址](https://blog.csdn.net/baidu_31657889/article/category/9059648)  
[github地址](https://github.com/aimi-cn/AILearners/tree/master/blog/Algorithm/jianzhi_offer)

## 二、题目

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

### 1、思路

思路1：对数组排序，找数组中间的数。如果一个数字出现的次数超过数组长度的一半，那么排序之后这个数肯定在最中间，然后使用count方法查看这个数出现的次数，大于数组长度一半的话，就返回这个数，否则返回0。

思路2：如果有符合条件的数字，则它出现的次数比其他所有数字出现的次数和还要多。
在遍历数组时保存两个值：一是数组中一个数字，一是次数。遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；若次数为0，则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。然后再判断它是否符合条件即可。
这实际上就是“分形叶”法，对数组同时去掉两个不同的数字，到最后剩下的一个数就是该数字。如果剩下两个，那么这两个也是一样的，就是结果，在其基础上把最后剩下的一个数字或者两个回到原来数组中，将数组遍历一遍统计一下数字出现次数进行最终判断。

### 2、编程实现

**python**

代码实现方案：

思路1：

```python
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numbers.sort()
        theone = numbers[len(numbers)/2]
        if numbers.count(theone) > len(numbers)/2:
            return theone
        return  0
```

思路2：

```python
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        res = numbers[0]
        times = 1
        length = len(numbers)
        for i in range(1, length):
            if times == 0:
                res = numbers[i]
                times = 1
            elif res == numbers[i]:
                times += 1
            else:
                times -= 1
    
        import collections
        return res if collections.Counter(numbers)[res] * 2 > length else 0
```
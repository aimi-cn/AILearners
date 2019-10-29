# LeetCode初级算法--设计问题02：最小栈

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

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

- push(x) -- 将元素 x 推入栈中。
- pop() -- 删除栈顶的元素。
- top() -- 获取栈顶元素。
- getMin() -- 检索栈中的最小元素。

**示例:**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```

### 1、思路

第一种方法：

用列表模拟栈，push、pop、top和getMin分别对应list.append()、list.pop()、list[-1]和min()操作

第二种方法：

引入minStack列表存放最小值

### 2、编程实现

第一种方法：

**python**

```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x is None:
            pass
        else:
            self.l.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.l is None:
            return 'error'
        else:
            self.l.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        if self.l is None:
            return 'error'
        else:
            return self.l[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.l is None:
            return 'error'
        else:
            return min(self.l)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

第二种方法：

```python
class MinStack(object):
 
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []       #存放所有元素
        self.minStack = []#存放每一次压入数据时，栈中的最小值（如果压入数据的值大于栈中的最小值就不需要重复压入最小值，小于或者等于栈中最小值则需要压入）
 
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minStack or self.minStack[-1]>=x:
            self.minStack.append(x)
 
    def pop(self):   #移除栈顶元素时，判断是否移除栈中最小值
        """
        :rtype: void
        """
        if self.minStack[-1]==self.stack[-1]:
            del self.minStack[-1]
        self.stack.pop()
 
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
```
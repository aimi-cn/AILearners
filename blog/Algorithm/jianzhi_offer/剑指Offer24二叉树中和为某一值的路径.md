# 剑指Offer（二十四）：二叉树中和为某一值的路径

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击CSDN链接：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)  
github地址：https://github.com/aimi-cn/AILearners/tree/master/blog/Algorithm/jianzhi_offer

## 二、题目

输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

### 1、思路

两个全局变量result和tmp，result来存放最终结果，tmp用来存放临时结果。

每次遍历，我们先把root的值拼接给tmp，然后判断当前root是否同时满足：

- 左子树不为空
- 右子树不为空
- 拼接的结果和是否和expectNumber值相等

如果满足条件，就将tmp拼接result中，否则，依次遍历左右子树。需要注意的是，遍历左右子树的时候，全局变量tmp是需要做回溯的，因为假如一个叶子结点的路径之和不符合要求我们是不是要回溯？是不是要把这个叶子结点擦掉然后回到父节点去访问另一个子节点。

### 2、编程实现

**python**

代码实现方案：

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        def subFindPath(root):
            if root:
                tmp.append(root.val)
                if not root.right and not root.left and sum(tmp) == expectNumber:
                    result.append(tmp[:])
                else:
                    subFindPath(root.left),subFindPath(root.right)
                # 回溯
                tmp.pop()
        result, tmp = [], []
        subFindPath(root)
        sorted(result, key=len, reverse=True)
        return result
```

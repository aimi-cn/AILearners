# 剑指Offer（三十八）：二叉树的深度

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击CSDN和github链接：  
[剑指Offer完整习题解析CSDN地址](https://blog.csdn.net/baidu_31657889/article/category/9059648)  
[github地址](https://github.com/aimi-cn/AILearners/tree/master/blog/Algorithm/jianzhi_offer)

## 二、题目

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

### 1、思路

使用递归的方法解决此题。直接上图：

![](../../../img/Algorithm/jianzhi_offer/jzoffer_38_01.png)

我们可以看到树的深度H等于1加上左右两个左右子树深度的最大值。

所以我们直接使用递归方法处理~看代码

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
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        # 使用递归
        # 如果该树只有一个结点，它的深度为1.如果根节点只有左子树没有右子树，
        # 那么树的深度为左子树的深度加1；同样，如果只有右子树没有左子树，
        # 那么树的深度为右子树的深度加1。如果既有左子树也有右子树，
        # 那该树的深度就是左子树和右子树的最大值加1.
        count = max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right)) + 1
        return count
```

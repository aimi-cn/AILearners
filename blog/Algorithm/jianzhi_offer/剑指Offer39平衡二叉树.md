# 剑指Offer（三十九）：平衡二叉树

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击CSDN和github链接：  
[剑指Offer完整习题解析CSDN地址](https://blog.csdn.net/baidu_31657889/article/category/9059648)  
[github地址](https://github.com/aimi-cn/AILearners/tree/master/blog/Algorithm/jianzhi_offer)

## 二、题目

输入一棵二叉树，判断该二叉树是否是平衡二叉树。

### 1、思路

如果二叉树的每个节点的左子树和右子树的深度不大于1，它就是平衡二叉树。

先写一个求深度的函数，再对每一个节点判断，看该节点的左子树的深度和右子树的深度的差是否大于1

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
    def IsBalanced_Solution(self, pRoot):
        # write code here
        # 每个节点的左子树和右子树的高度差至多为1。
        # 如果二叉树的每个节点的左子树和右子树的深度不大于1，它就是平衡二叉树。
        # 先写一个求深度的函数，再对每一个节点判断，看该节点的左子树的深度和右子树的深度的差是否大于1
        if not pRoot:
            return True
        if abs(self.maxDepth(pRoot.left) - self.maxDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    def maxDepth(self,pRoot):
        if not pRoot: return 0
        return max(self.maxDepth(pRoot.left), self.maxDepth(pRoot.right)) + 1
```

# LeetCode初级算法--树02：验证二叉搜索树

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

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

- 节点的左子树只包含小于当前节点的数。
- 节点的右子树只包含大于当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

**示例1:**

```
输入:
    2
   / \
  1   3
输出: true
```

**示例2:**

```
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
```

### 1、思路

- 为了验证一棵树是否是BST，我们可以一个节点一个节点的查看。
- 每一个节点都有一个最大值和最小值的范围。
- 哎？为什么一个节点有一个最大值和最小值的范围？
- 我们举个例子。

```
    5
   / \
  1   8
     / \
    3   10
```

在上述的树当中，1比5小，8比5大，第一层OK  
再第二层，3比8小，10比8大，OK....OK吗？  
不OK！因为3在5的右子树，应当比5大。  
所以不可以直观地认为一个节点只要比父节点大或者小就可以了，它实际上是由大小范围的。  
对于这个3,它应该的范围就是(5,8)。  
最大值和最小值怎么更新呢？  
很简单，如果要检查的节点在这个节点的左边，那么最大值就是这个节点的值，最小值就是上一轮检查当中的最小值。  
反之亦然。


### 2、编程实现

**python**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 初始化root的时候，它没有最大最小的限制
    def isValidBST(self, root: TreeNode, low = float('-inf'), high = float('inf')) -> bool:
        # 当这个节点不存在的时候，就返回True。就代表父节点没有（左或右）孩子
        if not root:return True
        # 判断当前节点是否大于最小值和小于最大值
        if not low<root.val<high:return False
        # 递归检查左右孩子，两个都为True才可以返回True
        return self.isValidBST(root.left,low,root.val) and self.isValidBST(root.right,root.val,high)
```
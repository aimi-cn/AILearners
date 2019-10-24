# LeetCode初级算法--树03：二叉树的层次遍历

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

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

**示例:**

```
给定二叉树: [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果:

```
[
  [3],
  [9,20],
  [15,7]
]
```

### 1、思路

使用递归的方法，广度遍历树，具体如下：

- 先定义一个空列表，并判断当前节点是否为空。如果为空，则返回该列表。
- 定义helper函数，用于递归二叉树。
- 将当前节点添加到列表中
- 递归该树的左右节点，直到遍历结束。

### 2、编程实现

**python**

```python
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        
        if not root:
            return result
        
        def helper(node, level):
            
            if len(result) == level:
                result.append([])

            result[level].append(node.val)
 
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return result
```

# 剑指Offer（十七）：树的子结构

> 搜索微信公众号:'AI-ming3526'或者'计算机视觉这件小事' 获取更多算法、机器学习干货  
> csdn：https://blog.csdn.net/baidu_31657889/  
> github：https://github.com/aimi-cn/AILearners

## 一、引子

这个系列是我在牛客网上刷《剑指Offer》的刷题笔记，旨在提升下自己的算法能力。  
查看完整的剑指Offer算法题解析请点击：[剑指Offer完整习题解析](https://blog.csdn.net/baidu_31657889/article/category/9059648)

## 二、题目

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

### 1、思路

要判断B是不是A的子结构，我们可以分为两部来做，第一步在树A中找到和B的根结点的值一样的结点R，第二步再判断树A中以R为根节点的子树是不是包含和树B一样的结构。

具体细节看代码~~~

在下面的代码中，我们递归调用HasSubtree遍历二叉树A。如果发现某一节点的值和树B的根结点的值相等，则调用DoesTree1HaveTree2,进行第二步判断。
第二步是判断树A中以R为跟结点的子树是不是和树B具有相同的结构。同样，我们也可以用递归的思路来考虑：如果节点R的值和树B的根节点不同，那么以R为根节点的子树和树B肯定不具有相同的节点；如果它们的值相同，那么递归地判断它们各自的左右节点的值是不是相同。递归的终止条件是到达了树A或者树B的叶子节点。
需要注意的是  DoesTree1HasTree2函数中，如果Tree2为空，则说明第二棵树遍历完了，即是第一颗树的子树，返回TRUE
如果tree1为空而tree2不为空说明tree2结构超大，tree1中不存在。

### 2、编程实现

**python2.7**

代码实现方案：

```python
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val==pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)
        return result

     def DoesTree1HaveTree2(self,pRoot_A,pRoot_B):
        if not pRoot_B:
            return True
        if not pRoot_A:
            return False
        if pRoot_A.val != pRoot_B.val:
            return False
         
        return self.DoesTree1HaveTree2(pRoot_A.left,pRoot_B.left) and self.DoesTree1HaveTree2(pRoot_A.right,pRoot_B.right)
```

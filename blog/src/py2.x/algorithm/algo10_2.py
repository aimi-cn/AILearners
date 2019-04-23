#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@author:bidongqinxian 
@github: https://github.com/bidongqinxian
'''

def mid_order(root):
    if root is None:
        return []
    result = [root.val]
    lefttree = self.mid_order(root.left)
    righttree = self.mid_order(root.right)
    return lefttree + result + righttree

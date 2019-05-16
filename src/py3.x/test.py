# -*- coding:UTF-8 -*-
# def longestCommonPrefix(strs):
#     if not strs: return ""
#     s1 = min(strs)
#     s2 = max(strs)
#     print(s1)
#     print(s2)
#     for i,x in enumerate(s1):
#         if x != s2[i]:
#             return s2[:i]
#     return s1

# def isValid(s):
#     ##如果是这样有效的字符必须会出现[]或者{}这样的 不断删除有效括号直到不能删除
#     while '{}' in s or '[]' in s or '()' in s:
#         print(s)
#         s = s.replace('{}','')
#         s = s.replace('[]','')
#         s = s.replace('()','')
#     return s == ''

# def mergeTwoLists(l1, l2):
# 每次选两个链表头结点最小的，
# 比如：我们生活中，有两个已经按照高矮排好的队伍，我们如何把变成一个队伍！当然，每次选两个队伍排头的，比较他们的高矮!组成新的的队伍。
#递归排序 
#     list1 = ((l1+l2))
#     return sorted(list1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1: return l2
#         if not l2: return l1
#         if l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next,l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1,l2.next)
#             return l2


if __name__ == "__main__":
    # strs = ["flower","slow","klight"]
    # print(longestCommonPrefix(strs))
    # s = "{[]}"
    # s1 = "([)]"
    # print(isValid(s1))
    # l1 = ListNode()
    # s1 = Solution()
    # print((s1.mergeTwoLists(l1,l1)))
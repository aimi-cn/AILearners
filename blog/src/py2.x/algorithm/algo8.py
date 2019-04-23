'''
This code is written by bidongqinxian
'''
def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return 
        cur1 = pHead1
        while cur1:
            cur2 = pHead2
            while cur2:
                if cur1.val == cur2.val:
                    return cur2
                cur2 = cur2.next
            cur1 = cur1.next
        return 

'''
This code is written by bidongqinxian
'''
def ReverseList(self, pHead):
    if not pHead or not pHead.next:
        return pHead         
    last = None         
    while pHead:
        tmp = pHead.next   
        pHead.next = last
        last = pHead
        pHead = tmp         
    return last

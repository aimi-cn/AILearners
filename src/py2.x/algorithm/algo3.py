'''
This code is written by bidongqinxian
'''
def Binary_Search(lst, num):
    lens = len(lst)-1
    firstid= 0
    lastid = lens
    while firstid <= lastid:
        middle = int(firstid + (lastid - firstid) / 2)
        if num < lst[middle]:
            lastid = middle - 1
        elif num > lst[middle]:
            firstid = middle + 1
        else:
            return middle
    return lastid

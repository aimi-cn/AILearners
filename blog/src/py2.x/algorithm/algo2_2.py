'''
This code is written by bidongqinxian
'''

def quick_sort(lst):
    if not lst:
        return []
    base = lst[0]
    left = quick_sort([x for x in lst[1: ] if x < base])
    right = quick_sort([x for x in lst[1: ] if x >= base])
    return left + [base] + right

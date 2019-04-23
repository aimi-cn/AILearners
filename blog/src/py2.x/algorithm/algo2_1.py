'''
This code is written by bidongqinxian
'''
def Partition(lst, left, right):
    baseline = lst[left]
    while left < right:
        while left < right and lst[right] >= baseline:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= baseline:
            left += 1
        lst[right] = lst[left]
    lst[left] = baseline
    return left

def quick_sort(lst, left, right):
    if left < right:
       base  = Partition(lst, left, right)
       q_sort(lst, left, base - 1)
       q_sort(lst, base + 1, right)
    return lst

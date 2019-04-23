'''
This code is written by bidongqinxian
'''
def merge(num1, num2):
    result = []
    i = j = 0
    while i < len(num1) and j < len(num2):
        if a[i] < b[j]:
            result.append(num1[i])
            i += 1
        else:
            result.append(num2[j])
            j += 1
    result += num1[i:]
    result += num2[j:]
    return result
 
def sort(data):
    lens = len(data)
    if lens <= 1:
        return data
    mid = length / 2
    num1 = sort (data[:mid])
    num2 = sort (data[mid:])
    return merge(num1, num2)

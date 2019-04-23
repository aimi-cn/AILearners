'''
This code is written by bidongqinxian
'''
def fib(n):
    if n <= 1:
        return n
    l_1 = 0
    l_2 = 1
    l = 1
    for i in range(2,n):
        l_i = l_i_1 + l_i_2
        l_i_2 = l_i_1
        l_i_1 = l_i
    return l_i

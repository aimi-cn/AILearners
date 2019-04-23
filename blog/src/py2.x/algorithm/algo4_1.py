'''
This code is written by bidongqinxian
'''
def Fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n >= 3:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

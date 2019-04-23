'''
This code is written by bidongqinxian
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        t2, t3, t5 = 0, 0, 0
        idx = 1
        array = [1]
        while idx < index:
            num = min(array[t2]*2, array[t3]*3, array[t5]*5)
            array.append(num)
            while array[t2]*2 <= num:
                t2 += 1
            while array[t3]*3 <= num:
                t3 += 1
            while array[t5]*5 <= num:
                t5 += 1
            idx += 1
        return array[index-1]

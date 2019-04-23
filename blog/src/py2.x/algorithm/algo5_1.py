'''
This code is written by bidongqinxian
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return False
        array = [1,2,3,5]
        while len(array)-1 < index:
            array = self.GetUglyNumber(array)
        array = sorted(array)
        return array[index-1]
         
    def GetUglyNumber(self, array):
        list2 = []
        for i in range(1,len(array)):
            for j in range(1,len(array)):
                new_num = array[i] * array[j]
                list2.append(new_num)
        array = array + list2
        array = list(set(array))
        return array

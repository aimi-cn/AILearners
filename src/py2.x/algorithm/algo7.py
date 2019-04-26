'''
This code is written by bidongqinxian
'''
def lengthOfLIS(lst):
        lens = len(lst)
        if not lst:
            return 0
        ones = [1 for _ in range(lens)]
        for j in range(1, lens):
            for i in range(1, j):
                if lst[j] > lst[i]:
                    ones[j] = max(ones[i]+ 1, ones[j] )  
        return max(ones)

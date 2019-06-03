#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/04/26 21:52:56
@Author  :   xiao ming 
@Version :   1.0
@Contact :   xiaoming3526@gmail.com
@Desc    :   None
@github  :   https://github.com/aimi-cn/AILearners
'''

# here put the import lib
'''
@description: 
@param {type} 
@return: 
'''
def test():
    1

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import numpy as np
np.zeros((2,3))


def reverseWords(s):
    return ' '.join(i[::-1] for i in s.split())
            

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(reverseWords(s))
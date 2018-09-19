# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Palindrome Number
from math import *
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0 : return False
        strX = str(abs(x))
        strX = '#' + '#'.join(strX) + '#'
        i = 0
        p = len(strX)/2
        while p-i>0:
            if strX[p-i]!=strX[p+i]:
                return False
            i+=1
        return True
        
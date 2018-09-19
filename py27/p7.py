# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Reverse Integer

from math import *
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxInt = 2147483647
        if x<0:
            strX = str(-x)
            strY = strX[::-1]
            y = -int(strY)
        else:
            strX = str(x)
            strY = strX[::-1]
            y = int(strY)
        if abs(y)<maxInt:return y   
        else: return 0
        
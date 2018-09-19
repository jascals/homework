# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        num = 0
        rval = 0
        for i in range(len(s)-1,-1,-1):
            num = num + dict[s[i]] if dict[s[i]] >= rval else num - dict[s[i]]
            rval = dict[s[i]]
        return num
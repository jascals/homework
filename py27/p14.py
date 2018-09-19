# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Longest Common Prefix

class Solution:  
    def longestCommonPrefix(self, strs):  
        if strs == []:  
            return ''  
        for i in range(len(strs[0])):  
            for str in strs:  
                if len(str) <= i or str[i] != strs[0][i]:  
                    return strs[0][:i]  
        return strs[0]  

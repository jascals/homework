# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Letter Combinations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):
        dicts = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':' ', '':''}
        l=[]
        for i in digits:
            l = self.cul(dicts[i], l)
        return l
    
    def cul(self, nums, l):
        item=[]
        for i in nums:
            if len(l)==0:
                item.append(i)
            for s in l:
                item.append(s+i)
        return item        
                
    

# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Generate Parentheses 

class Solution(object):
    def gp(self, n):
        self.s = []
        self.gpl('',n, n)
        return self.res
    def gpl(self, str, r, l):
        if r ==0 and l==0:self.s.append(str)
        if l>0:
            self.gpl(str+'(',r,l-1)
        if r>0 and r>l:
            self.gpl(str+')',r-1,l)
        
        

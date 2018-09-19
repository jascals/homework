# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Remove Element

class Solution(object):
    def removeElement(self, A, elem):  
        index = 0  
        for num in A:  
            if num != elem:  
                A[index] = num  
                index += 1  
        return index          
        

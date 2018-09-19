# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Remove Duplicates from Sorted Array

class Solution:  
    def removeDuplicates(self, A):  
        if len(A) == 0:  
            return 0  
        if len(A) == 1:  
            return 1    
        index = 0  
        for i in A[1:]:  
            if i != A[index]:  
                index += 1  
                A[index] = i  
        return index + 1   
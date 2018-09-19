# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Search Insert Position

class Solution(object):
    def searchInsert(self, A, target):
        left = 0; right = len(A) - 1
        while left <= right:
            mid = ( left + right ) / 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

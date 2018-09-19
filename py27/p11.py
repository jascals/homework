# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        maxm = 0
        j = 0
        k = size - 1
        while j < k:
            if height[j] <= height[k]:
                maxm = max(maxm,height[j] * (k - j))
                j += 1
            else:
                maxm = max(maxm,height[k] * (k - j))
                k -= 1
        return maxm
    

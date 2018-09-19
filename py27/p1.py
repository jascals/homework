# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# two sum

class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
			j=target-i
			if j in nums:
				if j!=i:
					index0=[x for x,a in enumerate(nums) if a==i][0]
					index1=[x for x,a in enumerate(nums) if a==j][0]
					return (index0,index1)
				elif j==i and len([x for x,a in enumerate(nums) if a==i])>1:
					index0=[x for x,a in enumerate(nums) if a==i][0]
					index1=[x for x,a in enumerate(nums) if a==i][1]
					return (index0,index1)
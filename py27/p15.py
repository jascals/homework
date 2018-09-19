# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Longest 3Sum

class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []
        if len(nums)<3:
            return []
        for y in xrange(len(nums)):
            if nums[y]>0:
                break
            if y > 0 and nums[y] == nums[y-1]:
                continue
            res = self.twoSum(nums,-nums[y], y, res)
        return res

    def twoSum(self, nums, target, y, res):
        dict={}
        for i in xrange(len(nums)):
            if y >=i:
                continue
            x=nums[i]
            if target-x in dict:
                mlist = sorted([target-x, x, nums[y]])
                if mlist in res:
                    continue
                res.append(mlist)
                continue
            dict[x]=i
        return res
# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Search for a Range

class Solution(object):
    def findLeft(self,nums,first,mid):
        if nums[first] == nums[mid]:
            return first
        nmid = (first + mid) // 2
        if nums[nmid] == nums[mid]:
            return self.findLeft(nums,first,nmid)
        return self.findLeft(nums,nmid + 1,mid)
    def findRight(self,nums,mid,last):
        if nums[last] == nums[mid]:
            return last
        nmid = (mid + last + 1) // 2
        if nums[nmid] == nums[mid]:
            return self.findRight(nums,nmid,last)
        return self.findRight(nums,mid,nmid - 1)
    def searchRange(self, nums, target):
        last = len(nums);first = 0
        while first != last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return [self.findLeft(nums,first,mid),self.findRight(nums,mid,last - 1)]
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid
        return [-1,-1]

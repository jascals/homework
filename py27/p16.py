# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Longest 3Sum Closest

class Solution:  
    def threeSumClosest(self, nums, target):  
        length=len(nums);Min=2147483647  
        nums.sort()  
        for i in range(length-2):  
            if i>0 and nums[i]==nums[i-1]:continue  
            begin=i+1;end=length-1  
            while begin<end:  
                sum=nums[i]+nums[begin]+nums[end]  
                if abs(sum-target)<abs(Min):Min=sum-target  
                if sum==target:return target  
                elif sum>target:end-=1  
                else:begin+=1  
        return Min+target  

# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# add two number

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from math import pow

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans=[]
        ech=0
        coin=0
        while 1:
            if l1==None and l2==None:break
            if l1!=None:
                ech+=l1.val
                l1 = l1.next
            if l2!=None:
                ech+=l2.val
                l2 = l2.next
            ech += coin
            coin = ech/10
            ans.append(ech%10)
            ech=0
        if coin>0:
        	ans.append(coin)
        return ans[:]

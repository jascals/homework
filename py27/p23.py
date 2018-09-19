# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Merge k Sorted Lists

class Solution:  
    def mergeKLists(self, lists):  
        if len(lists) == 0:  
            return None  
        if len(lists) == 1:  
            return lists[0]  
  
        mid = len(lists) // 2  
        l1 = self.mergeKLists(lists[:mid])  
        l2 = self.mergeKLists(lists[mid:])  
  
        # merge Two Lists  
    
        nl = ListNode(0)  
        c = nl  
        while l1 and l2:  
            if l1.val <= l2.val:  
                c.next = l1  
                l1 = l1.next  
            else:  
                c.next = l2  
                l2 = l2.next  
            c = c.next 
        c.next = l1 or l2  
        return nl.next  
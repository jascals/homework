# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Merge Two Sorted Lists 

class Solution:  
    def mergeTwoLists(self, l1, l2):  
        if not l1 and not l2:  
            return None  
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

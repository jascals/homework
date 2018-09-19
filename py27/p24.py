# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Swap Nodes in Pairs

class Solution:
    def swapPairs(self, head):
        ln = ListNode(0)
        ln.next = head
        p, c = ln, head
        while c and c.next:       
            p.next = c.next        
            c.next = p.next.next   
            p.next.next = c        
            p, c = c,c.next  
        return ln.next
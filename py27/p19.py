# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Remove Nth Node From End of List

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fn=ListNode(0); 
        fn.next=head
        p1=p2=fn
        for i in range(n): 
            p1=p1.next
        while p1.next:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return fn.next
        
        

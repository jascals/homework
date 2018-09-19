# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):  
        p=ListNode(0)  
        p.next=head;head=p;s=p  
        len=k  
        while k>0 and s!=None:k-=1;s=s.next  
        while s!=None:  
            flag=s.next;tail=p.next;l=p.next  
            while l!=flag:  
                tmp=p.next  
                p.next=l  
                l=l.next  
                p.next.next=tmp  
            tail.next=l  
            p=tail;s=tail  
            k=len  
            while k>0 and s!=None:k-=1;s=s.next  
        return head.next    
            

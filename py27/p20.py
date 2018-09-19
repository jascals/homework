# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Valid Parentheses

class Solution(object):
    def isValid(self, s):
        fm = {')': '(', '}': '{', ']': '['}
        stack = [None]
        for c in s:
            if c in fm and fm[c] == stack[len(stack)-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 1
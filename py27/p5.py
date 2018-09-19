# -*- coding:utf-8 -*-
# author cherie
# jascal@163.com
# jascal.net

# Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s);
        if length <= 1:
            return s;
        num = 0;
        font = 0;
        back = 0;
        max = 0;
        res1 = 0;
        res2 = 0;
        i = 0;
        for i in range(length):
            
            font = i - 1;
            back = i + 1;
            while font >= 0 and back < length:
                if s[font] == s[back]:
                    font -= 1;
                    back += 1;
                else:
                    
                    font += 1;
                    back -= 1;
                    break;
            else:
                
                font += 1;
                back -= 1;
            if font < back and font >= 0 and back < length:
                pass;
            else:
                
                font = i;
                back = i;
            num = back - font;
            if num >= max:
                max = num;
                res1 = font;
                res2 = back;
            
            if i + 1 < length and s[i] == s[i + 1]:
                font = i - 1;
                back = i + 2;
                while font >= 0 and back < length:
                    if s[font] == s[back]:
                        font -= 1;
                        back += 1;
                    else:
                        font += 1;
                        back -= 1;
                        break;
                else:
                    font += 1;
                    back -= 1;
                if font < back and font >= 0 and back < length:
                    pass;
                else:
                    font = i;
                    back = i + 1;
                num = back - font;
                if num >= max:
                    max = num;
                    res1 = font;
                    res2 = back;
        return s[res1:res2 + 1];
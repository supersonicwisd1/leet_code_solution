"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        reversed_x = x[::-1]
        if x :
            return x == reversed_x
        return False
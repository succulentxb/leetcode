#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for subLen in range(len(s), -1, -1):
            for start in range(len(s)-subLen+1):
                if isPalindrome(s[start:start+subLen]):
                    return s[start:start+subLen]
        return None

def isPalindrome(s: str) -> bool:
    slen = len(s)
    for i in range(int(slen/2)):
        if s[i] != s[slen-1-i]:
            return False
    return True

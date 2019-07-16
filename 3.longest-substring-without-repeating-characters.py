#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLen = 0
        subStrCharIdx = {}
        for curr in range(0, len(s)):
            idx = subStrCharIdx.get(s[curr])
            if idx is not None:
                for i in range(start, idx+1):
                    subStrCharIdx[s[i]] = None
                subStrCharIdx[s[curr]] = curr
                start = idx+1
                continue
            subStrCharIdx[s[curr]] = curr
            if curr-start+1 > maxLen:
                maxLen = curr-start+1
        return maxLen
            


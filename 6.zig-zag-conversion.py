#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        result = ""
        step = numRows*2 - 2
        for i in range(0, len(s), step):
            result += s[i]
        for j in range(1, numRows-1):
            former = ""
            for i in range(j, len(s), step):
                former += s[i]
            latter = ""
            for i in range(step-j, len(s), step):
                latter += s[i]
            last = -1
            for i in range(len(latter)):
                result += former[i] + latter[i]
                last = i
            if last < len(former)-1:
                result += former[-1]
        for i in range(numRows-1, len(s), step):
            result += s[i]
        return result


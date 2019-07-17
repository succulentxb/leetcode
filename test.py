def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    maxLen = 0
    subStrCharIdx = {}
    for curr in range(0, len(s)):
        idx = subStrCharIdx.get(s[curr])
        if idx is not None:
            start = idx+1
            subStrCharIdx = {}
            for i in range(start, curr+1):
                subStrCharIdx[s[i]] = i
            continue
        subStrCharIdx[s[curr]] = curr
        if curr-start+1 > maxLen:
            maxLen = curr-start+1
    return maxLen

def convert(s: str, numRows: int) -> str:
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

if __name__ == "__main__":
    print(convert("AB", 3))
    

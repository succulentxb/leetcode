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


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
    

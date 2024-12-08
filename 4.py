class Solution: 
    def lengthOfLongestSubstring(self, s):
        m = 0
        l = 0
        for r in range(len(s)):
            for i in range(l, r):
                if s[i] == s[r]:
                    l = i + 1
                    break
            m = max(m, r - l + 1)        
        return m
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
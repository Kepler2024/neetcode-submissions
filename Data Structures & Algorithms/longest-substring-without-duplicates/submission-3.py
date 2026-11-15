class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxL = 0
        while (r<len(s)):
            while s[r] in s[l:r]:
                l += 1
            maxL = max(r-l+1, maxL)
            r += 1
        return maxL

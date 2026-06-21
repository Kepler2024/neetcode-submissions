class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_S = {}
        for c in s:
            if c in count_S:
                count_S[c] += 1
            else:
                count_S[c] = 0
        count_T = {}
        for b in t:
            if b in count_T:
                count_T[b] += 1
            else:
                count_T[b] = 0
        return count_S == count_T
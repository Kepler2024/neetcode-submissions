class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            if tuple(cnt) not in res:
                res[tuple(cnt)] = [s]
            else:
                res[tuple(cnt)].append(s)
        return list(res.values())

        

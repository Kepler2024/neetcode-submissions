class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visit = [0] * len(strs)
        res = []
        for i, s in enumerate(strs):
            if  not visit[i]:
                visit[i] = 1
                tmp = [s]
                for j, st in enumerate(strs):
                    if (not visit[j]) and (sorted(st)==sorted(s)):
                        visit[j] = 1
                        tmp.append(st)
                res.append(tmp)
        return res
        
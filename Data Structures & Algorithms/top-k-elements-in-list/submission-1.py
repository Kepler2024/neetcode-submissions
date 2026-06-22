class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        res = []

        while (k):
            max = float("-inf")
            maxN = None
            for n,v in cnt.items():
                if v > max:
                    max = v
                    maxN = n
            res.append(maxN)
            cnt.pop(maxN)
            k -= 1

        return res
        
        

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num,0)

        sort = sorted(cnt.items(), key = lambda x:x[1],reverse=True)[:k]
        # res = []
        # for t in sort:
        #     res.append(t[0])
        res = [num for num,fre in sort]
        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num,0)

        f = [[] for i in range(len(nums) + 1)]
        for num,fre in cnt.items():
            f[fre].append(num)
        
        res = []
        for i in range(len(f)-1, -1, -1):
            if not f[i]==[]:
                for num in f[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        
            
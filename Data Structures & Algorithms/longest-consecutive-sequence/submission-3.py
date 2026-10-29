class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        res = 0
        for num in arr:
            if (num-1) not in arr:
                len = 1
                while (num+1) in arr:
                    num += 1
                    len += 1
                res = max(res,len)
        return res
        
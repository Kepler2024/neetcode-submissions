class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums) #  in in set : O(1)
      # arr = list(set(nums)) in in list : O(n) 
        res = 0
        for num in arr:
            if (num-1) not in arr:
                len = 1
                while (num+len) in arr:
                    len += 1
                res = max(res,len)
        return res
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        prefix = 1
        for i in range(0,l,1):
            res[i] = prefix 
            prefix *= nums[i]

        suffix = 1
        for j in range(l-1,-1,-1):
            res[j] *= suffix
            suffix *= nums[j]
        
        return res
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l<r:
            m = l + (r-l) // 2 # 二分查找，就是不断缩减范围，改范围就行了
            if nums[m] > nums[r]: # 断点在m~r之间
                l = m+1
                continue
            elif nums[m] <= nums[r]: # 断点在l~m之间
                r = m
                continue
        return nums[r]
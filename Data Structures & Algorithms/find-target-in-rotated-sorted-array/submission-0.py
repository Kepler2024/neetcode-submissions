class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l<r: #二分查找，最后会缩成l=r
            m = l + (r-l) // 2 # 二分查找，就是不断缩减范围，改范围就行了
            if nums[m] > nums[r]: # 断点在m~r之间
                l = m+1
                continue
            elif nums[m] <= nums[r]: # 断点在l~m之间
                r = m
                continue
        mi = r
        l = 0
        r = mi

        while l<=r:
            m = l+(r-l) //2
            if nums[m] > target: 
                r = m - 1
                continue
            elif nums[m] < target: 
                l = m + 1
                continue
            elif nums[m] == target:
                return m
        
        l = mi
        r = len(nums) - 1
        while l<=r:
            m = l+(r-l) //2
            if nums[m] > target: 
                r = m - 1
                continue
            elif nums[m] < target: 
                l = m + 1
                continue
            elif nums[m] == target:
                return m

        return -1
        
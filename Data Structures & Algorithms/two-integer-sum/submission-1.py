class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        br = 0
        a=None
        b=None
        for i in range (0,l):
            for j in range (i+1,l):
                if (nums[i]+nums[j]==target):
                    br = 1
                    a = i
                    b = j
                if (br==1):
                    break
                j+=1
            if (br==1):
                break
            i+=1
        return [a,b]

        
        
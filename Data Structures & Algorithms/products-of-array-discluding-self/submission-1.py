import sys
sys.setrecursionlimit(300000)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        def go(i: int, prefix: int) -> int:
            # prefix = nums[0..i-1] 的乘积（递推：L[i] = L[i-1] * nums[i-1]）
            if i == n:
                return 1                      # 空后缀积 = 1（初始值）
            suffix = go(i + 1, prefix * nums[i])  # 返回 nums[i+1..n-1] 的乘积
            res[i] = prefix * suffix
            return suffix * nums[i]           # R 递推：R[i-1] = R[i] * nums[i]

        go(0, 1)
        return res
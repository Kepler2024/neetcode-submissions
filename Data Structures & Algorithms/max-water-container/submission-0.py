class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while (l<r):
            s = min(heights[l],heights[r]) * (r-l)
            res = max(s, res)
            if (heights[l] <= heights[r]):
                l += 1
                continue
            else:
                r -= 1
                continue
        return res
        
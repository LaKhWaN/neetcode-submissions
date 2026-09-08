class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            min_height = min(heights[l], heights[r])
            area = max(area, min_height * (r-l))

            if heights[l] < heights[r]: l += 1
            else: r -= 1
        return area
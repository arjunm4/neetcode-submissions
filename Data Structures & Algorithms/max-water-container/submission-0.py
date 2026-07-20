class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        lp, rp = 0, len(heights) - 1
        
        while lp < rp:
            width = rp - lp
            height = min(heights[lp], heights[rp])
            curr_area = width * height
            if curr_area > max_area:
                max_area = curr_area
            if heights[lp] > heights[rp]:
                rp -= 1
            else:
                lp += 1
        
        return max_area
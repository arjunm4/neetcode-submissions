class Solution:
    def trap(self, height: List[int]) -> int:

        lp, rp = 0, len(height) - 1
        pre_max, suff_max = height[lp], height[rp]
        max_water = 0
        while lp < rp:
            if height[lp] < height[rp]:
                lp += 1
                pre_max = max(pre_max, height[lp])
                max_water += pre_max - height[lp]
            else:
                rp -= 1
                suff_max = max(suff_max, height[rp])
                max_water += suff_max - height[rp]
        
        return max_water
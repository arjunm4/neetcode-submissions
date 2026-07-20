class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        prefix = [0] * length
        curr_max = 0
        for i in range(len(height)):
            prefix[i] = curr_max
            curr_max = max(curr_max, height[i])

        suffix = [0] * length
        curr_max = 0
        for i in range(len(height) - 1, -1, -1):
            suffix[i] = curr_max
            curr_max = max(curr_max, height[i])
        
        max_water = 0

        for i in range(len(height)):
            curr_water = min(prefix[i], suffix[i]) - height[i]
            if curr_water > 0:
                max_water += curr_water
        
        return max_water
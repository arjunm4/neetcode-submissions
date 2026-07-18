class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 in seen:
                continue
            length = 1
            j = 1
            while True:
                if nums[i] + j not in seen:
                    break
                else:
                    length += 1
                    j += 1
            if length > longest:
                longest = length
        return longest
            
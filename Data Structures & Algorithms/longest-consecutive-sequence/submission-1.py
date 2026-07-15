class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_seq = 0
        for num in nums:
            if num - 1 not in nums:
                sub_seq = 1
                while num + sub_seq in nums:
                    sub_seq += 1
                longest_seq = max(longest_seq, sub_seq)
        return longest_seq
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = []
        for num in nums:
            if num in self.seen_nums:
                return True
            seen_nums.append(num)
        return False
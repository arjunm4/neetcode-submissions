class Solution:
    seen_nums = []
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if num in self.seen_nums:
                return True
            self.seen_nums.append(num)
        return False
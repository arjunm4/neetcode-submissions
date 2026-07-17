class Solution:
    # input = [1, 2, 4, 6]
    # prefix = [1, 1, 2, 8]
    # suffix = [48, 24, 6, 1]


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1

        for i in range(len(nums)):
            prefix.append(product)
            product *= nums[i]
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= product
            product *= nums[i]
        
        return prefix
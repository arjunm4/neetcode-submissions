class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            mid = (lp + rp) // 2

            if nums[mid] == target: # found
                return mid 
            
            if nums[lp] <= nums[mid]: # left side is sorted
                if target > nums[mid] or target < nums[lp]: # target not in left
                    lp = mid + 1
                else:
                    rp = mid - 1
            else: # right side is sorted
                if target > nums[rp] or target < nums[mid]: # target not in right
                    rp = mid - 1
                else:
                    lp = mid + 1
        
        return -1

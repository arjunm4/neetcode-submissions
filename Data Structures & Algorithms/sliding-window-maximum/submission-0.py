class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque()

        lp = rp = 0

        while rp < len(nums):
            
            while queue and nums[rp] > nums[queue[-1]]:
                queue.pop()

            queue.append(rp)

            if lp > queue[0]:
                queue.popleft()
            
            if rp + 1 >= k:
                result.append(nums[queue[0]])
                lp += 1

            rp += 1

        return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == k:
            return list(set(nums))

        frequency = {}

        for i in range(len(nums)):
            cur_num = nums[i]
            if cur_num in frequency:
                frequency[cur_num] += 1
            else:
                frequency[cur_num] = 1
        print(frequency)
        ans = []
        while k > 0:
            for num, frq in frequency.items():
                if frq == max(frequency.values()) :
                    ans.append(num)
                    del frequency[num]
                    break
            k -= 1
        return ans
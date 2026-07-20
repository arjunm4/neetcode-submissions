class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        lp, rp = 0, 0
        max_length = 0

        while rp < len(s):
            if s[rp] not in seen:
                seen.add(s[rp])
                rp += 1
                max_length = max(max_length, rp - lp)
            else:
                seen.remove(s[lp])
                lp += 1

        return max_length

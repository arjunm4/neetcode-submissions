class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        result = 0
        maxf = 0

        lp = 0
        for rp in range(len(s)):
            count[s[rp]] += 1
            maxf = max(maxf, count[s[rp]])

            while (rp - lp + 1) - maxf > k:
                count[s[lp]] -= 1
                lp += 1
            
            result = max(result, (rp - lp + 1))
        
        return result
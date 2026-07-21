class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        window = defaultdict(int)

        have, need = 0, len(count)
        result, result_len = [-1, -1], float("inf")

        lp = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in count and window[char] == count[char]:
                have += 1
            
            while have == need:
                if (r - lp + 1) < result_len:
                    result = [lp, r]
                    result_len = (r - lp + 1)
                window[s[lp]] -= 1
                if s[lp] in count and window[s[lp]] < count[s[lp]]:
                    have -= 1
                lp += 1

        l, r = result
        return s[l:r+1]
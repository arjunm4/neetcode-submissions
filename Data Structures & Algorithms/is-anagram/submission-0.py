class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            cur_s = s_map[s[i]] + 1 if s[i] in s_map else 1
            cur_t = t_map[t[i]] + 1 if t[i] in t_map else 1
            s_map[s[i]] = cur_s
            t_map[t[i]] = cur_t
        return s_map == t_map

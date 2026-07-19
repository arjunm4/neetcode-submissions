class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = set("abcdefghijklmnopqrstuvwxyz0123456789")
        lower_s = s.lower()
        
        lp, rp = 0, len(lower_s) - 1

        while lp < rp:
            while lp < rp and lower_s[lp] not in alphanum:
                lp += 1
            while lp < rp and lower_s[rp] not in alphanum:
                rp -= 1
            if lower_s[lp] == lower_s[rp]:
                lp += 1
                rp -= 1
                continue
            else:
                return False

        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_s = ''
        for char in s:
            if char.isalnum():
                modified_s += char.lower()
        return modified_s == modified_s[::-1]
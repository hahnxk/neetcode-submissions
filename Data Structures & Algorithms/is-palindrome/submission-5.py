class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        s_reversed = s[::-1]
        if s_reversed == s:
            return True
        else:
            return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()]).lower()
        reverse_s = s[::-1]
        if s == reverse_s:
            return True
        return False
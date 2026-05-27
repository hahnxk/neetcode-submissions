class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove not alphanumeric chars from s
        s = "".join([char for char in s if char.isalnum()]).lower()
        # Store reverse s in another string variable
        reverse_s = s[::-1]
        # Compare original string and reversed string
        if s == reverse_s:
            return True
        return False
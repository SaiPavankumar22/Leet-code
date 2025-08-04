class Solution:
    def isPalindrome(self, s: str) -> bool:
        joi = ''.join(c.lower() for c in s if c.isalnum())
        return joi == joi[::-1]
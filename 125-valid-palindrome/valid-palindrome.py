class Solution:
    def isPalindrome(self, s: str) -> bool:
        k =""
        for i in s:
            if(i.isalpha()):
                k+=i.lower()
            elif(i.isdigit()):
                k+=i
        
        if(k == k[::-1]):
            return True
        return False
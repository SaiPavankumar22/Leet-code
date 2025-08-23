class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        c = list(s)
        l = 0
        r = len(s) - 1
        
        while l < r:
            if not c[l].isalpha():
                l += 1
            elif not c[r].isalpha():
                r -= 1
            else:
                c[l], c[r] = c[r], c[l]
                l += 1
                r -= 1
        
        return ''.join(c)
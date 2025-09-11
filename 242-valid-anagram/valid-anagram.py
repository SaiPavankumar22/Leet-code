class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k = Counter(s)
        t = Counter(t)
        if(k == t):
            return True
        else:
            return False
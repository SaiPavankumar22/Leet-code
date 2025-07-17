class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        g = s.split(" ")
        i=-1
        while (g[i]==""):
            i-=1
        r = g[i]
        p=len(r)
        return p
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        greedy = 0
        sizei = 0
        while(greedy<len(g) and sizei<len(s)):
            if(s[sizei]>=g[greedy]):
                greedy+=1
            sizei+=1
        return greedy

class Solution:
    def maxDepth(self, s: str) -> int:
        a=0
        res=0
        for i in s:
            if(i=='('):
                a+=1
            elif(i==')'):
                a-=1
            res=max(res,a)
        return res
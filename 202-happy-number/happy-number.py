class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def chk(n):
            if(n==1):
                return True
            if(n in s):
                return False
            s.add(n)
            res = 0
            for i in str(n):
                res+=(int(i))**2
            return chk(res)
        return chk(n)

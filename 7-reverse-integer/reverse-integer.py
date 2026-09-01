class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        cnt = 0
        tmp = ""
        res= 0
        if(s[0]=="-"):
            cnt+=1
            tmp = s[1:]
            k="-" + tmp[::-1]
            res = int(k)
        else:
            res= int(s[::-1])
        if(res<-2147483648 or res>2147483647):
            return 0
        else: 
            return res


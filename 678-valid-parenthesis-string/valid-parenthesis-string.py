class Solution:
    def checkValidString(self, s: str) -> bool:
        mi_open = 0
        ma_open = 0
        for i in s:
            if(i=='('):
                mi_open+=1
                ma_open+=1
            elif(i==')'):
                mi_open-=1
                ma_open-=1
            else:
                mi_open-=1
                ma_open+=1
            
            if(ma_open<0):
                return False
            mi_open = max(mi_open,0)
        return mi_open == 0
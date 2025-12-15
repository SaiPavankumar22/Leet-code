class Solution:
    def maxFreqSum(self, s: str) -> int:
        vol = 0
        con = 0
        sets = set(s)
        for i in sets:
            if(i in 'AEIOUaeiou'):
                vol = max(vol,s.count(i))
            else:
                con = max(con,s.count(i))
        return vol+con
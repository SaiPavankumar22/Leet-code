class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            freq ={}
            for j in range(i,len(s)):
                if(s[j] in freq):
                    freq[s[j]]+=1
                else:
                    freq[s[j]]=1
                val = freq.values()
                mi = min(val)
                ma = max(val)
                res+=(ma-mi)
        return res
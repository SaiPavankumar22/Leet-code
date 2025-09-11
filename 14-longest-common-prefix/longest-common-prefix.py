class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        h= len(strs[0])
        res=""
        for a in strs:
            if(len(a)<h):
                h = len(a)

        for i in range(0,h):
            k = strs[0][i]
            for j in range(1,len(strs)):
                if(strs[0][i] != strs[j][i]):
                    return res
            res+=k
        return res
                
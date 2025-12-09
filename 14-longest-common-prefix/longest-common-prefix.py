class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        st = strs[0]
        en = strs[-1]
        res = []
        for i in range(min(len(st),len(en))):
            if(st[i]!=en[i]):
                return ''.join(res)
            res.append(st[i])

        return ''.join(res)
        
                
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        k={}
        for i in licensePlate:
            if(i.isalpha()):
                i = i.lower()
                if(i in k):
                    k[i]+=1
                else:
                    k[i]=1
        
        mi = float('inf')
        res = None
        for j in words:
            d={}
            for c in j:
                if(c in d):
                    d[c]+=1
                else:
                    d[c]=1
            h = True
            for a,b in k.items():
                if a in d:
                    if(d[a]<b):
                        h = False
                        break
                else:
                    h = False
                    break
            if(h and len(j)<mi):
                res = j
                mi = len(j)
        return res


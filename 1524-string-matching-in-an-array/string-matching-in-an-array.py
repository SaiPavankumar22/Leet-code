class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        k=[]
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if(words[i] == words[j]):
                    pass
                elif(words[i] in words[j]):
                    k.append(words[i])
                elif(words[j] in words[i]):
                    k.append(words[j])
                else:
                    pass
        return list(set(k))


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s= ""
        for i in word1:
            s = s+i
        k=""
        for j in word2:
            k = k+j
        if(s == k):
            return True
        else:
            return False
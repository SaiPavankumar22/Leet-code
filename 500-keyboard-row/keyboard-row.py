class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = "qwertyuiop"
        s = "asdfghjkl"
        t = "zxcvbnm"
        k = []
        for i in words:
            j = i.lower()
            if(len(set(f+j))==len(f) or len(set(s+j))==len(s) or len(set(t+j))==len(t)):
                k.append(i)
        return k

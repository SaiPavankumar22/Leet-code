from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        r=""
        k = Counter(s)
        for i,j in k.most_common():
            r+=(i*j)
        return r
from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        k = Counter(candyType)
        m=len(k)
        if(len(candyType)/2 <=m):
            return int(len(candyType)/2)
        else:
            return m
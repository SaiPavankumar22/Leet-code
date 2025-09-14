class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = set(jewels)
        count = 0
        for i in stones:
            if(i in res):
                count +=1
        return count
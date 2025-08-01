class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        k = sorted(heights)
        c = 0
        for i in range(0,len(k)):
            if(heights[i] != k[i]):
                c+=1
        return c
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        tol = 0
        for i in range(len(timeSeries)-1):
            j = timeSeries[i+1] - timeSeries[i]
            m = min(duration, j)
            tol+=m
        tol+=duration
        return tol


        
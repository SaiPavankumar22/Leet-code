class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<1):
            return False
        x = math.log10(n) / math.log10(3)
        return x == int(x)
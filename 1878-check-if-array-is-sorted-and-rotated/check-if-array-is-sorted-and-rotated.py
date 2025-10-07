class Solution:
    def check(self, nums: List[int]) -> bool:
        k = nums.copy()
        k.sort()
        if(k == nums):
            return True
        n = False
        for i in range(0,len(nums)):
            a = k[-1]
            k.pop()
            k.insert(0,a)
            if(k == nums):
                return True
        return n
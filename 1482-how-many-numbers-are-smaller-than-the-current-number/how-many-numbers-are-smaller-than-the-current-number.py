class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k = sorted(nums)
        h=[]
        for i in nums:
            p=k.index(i)
            h.append(p)
        return h
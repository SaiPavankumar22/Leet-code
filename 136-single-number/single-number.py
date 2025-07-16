class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k=[]
        for i in nums:
            if i not in k:
                k.append(i)
            else:
                k.remove(i)
        return k[0]
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(a):
            k=list(str(a))
            m = max(k)
            e = m* len(k)
            return int(e)
        for f in range(len(nums)):
            nums[f]=encrypt(nums[f])
        return sum(nums)

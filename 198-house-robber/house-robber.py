class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        pre = nums[0]
        pre2 = 0
        for i in range(1,n):
            pick = nums[i]
            if(i>1):
                pick+=pre2
            notpick = 0 + pre
            cur = max(pick,notpick)
            pre2 = pre
            pre=cur
        return pre
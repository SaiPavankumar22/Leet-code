class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        right = 0
        left = 0
        maxlen = 0
        zero = 0 
        while(right<len(nums)):
            if(nums[right]==0):
                zero +=1
            if(zero>k):
                if(nums[left]==0):
                    zero -= 1
                left+=1
            if(zero<=k):
                maxlen = max(maxlen, right-left+1)
            right+=1
        return maxlen
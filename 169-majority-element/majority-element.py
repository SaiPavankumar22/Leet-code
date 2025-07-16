class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict ={}
        for i in nums:
            if(i in dict):
                dict[i]+=1
            else:
                dict[i]=1
        ma=0
        k=0
        for key,value in dict.items():
            if(value>ma):
                ma=value
                k=key
        return k
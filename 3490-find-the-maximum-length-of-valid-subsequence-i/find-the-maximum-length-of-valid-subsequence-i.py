class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        eve = 0
        for i in nums:
            if(i%2==0):
                eve+=1
        od=0
        for j in nums:
            if(j%2==1):
                od+=1
        
        st_eve = 0
        rem1 = 0
        for q in nums:
            if(q%2==rem1):
                st_eve+=1
                rem1 ^=1
        st_odd = 0
        rem2 = 1
        for w in nums:
            if(w%2==rem2):
                st_odd +=1
                rem2 ^=1

        return max(eve, od, st_eve, st_odd)
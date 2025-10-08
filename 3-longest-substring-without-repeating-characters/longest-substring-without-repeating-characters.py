class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maps = [-1] * 256
        left = 0
        right = 0
        length = 0
        n = len(s)
        while(right<n):
            if(maps[ord(s[right])] != -1):
                left = max(maps[ord(s[right])]+1, left)
            maps[ord(s[right])] = right
            length = max(length,right-left+1)
            right+=1
        return length
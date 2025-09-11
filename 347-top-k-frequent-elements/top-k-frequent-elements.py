class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        common = s.most_common(k)
        res =[]
        for i , j in common:
            res.append(i)
        return res
        
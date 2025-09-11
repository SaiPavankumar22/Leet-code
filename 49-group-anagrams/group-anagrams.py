class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            k = "".join(sorted(i))
            res[k].append(i)
        return list(res.values(
        ))
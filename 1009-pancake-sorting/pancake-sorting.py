class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for curr in range(n,1,-1):
            idx = 0
            for i in range(1,curr):
                if(arr[i]> arr[idx]):
                    idx = i
            if(idx == curr - 1):
                continue
            if(idx!=0):
                res.append(idx+1)
                arr[:idx + 1] = arr[:idx +1][::-1]

            res.append(curr)
            arr[:curr] = arr[:curr][::-1]
        return res
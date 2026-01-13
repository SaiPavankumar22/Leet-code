class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        min_y, max_y = float('inf'), float('-inf')
        
        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
            
        target = total_area / 2.0
        
        def get_area_above(k):
            area = 0.0
            for x, y, l in squares:
                top = y + l
                if k <= y:
                    area += l * l
                elif k < top:
                    area += (top - k) * l
            return area

        low, high = min_y, max_y
        for _ in range(100):
            mid = (low + high) / 2
            if get_area_above(mid) > target:
                low = mid
            else:
                high = mid
                
        return low
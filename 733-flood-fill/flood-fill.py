class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        r = image[sr][sc]
        if(r == color):
            return image
        def dfs(sr,sc,color):
            if(sr<0 or sc<0 or sr>= row or sc>= col):
                return
            if(image[sr][sc]!= r):
                return
            image[sr][sc] = color
            dfs(sr+1, sc, color)
            dfs(sr-1, sc, color)
            dfs(sr, sc+1, color)
            dfs(sr, sc-1, color)
        dfs(sr, sc, color)
        return image
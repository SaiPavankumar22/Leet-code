class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def dfs(part,tile):
            if(part):
                res.add(part)
            for i in range(len(tile)):
                dfs(part+tile[i],tile[:i]+tile[i+1:])
        dfs('',tiles)
        return len(res)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        res = [[0] * m for _ in range(n)]
        vis = [[0] * m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    vis[i][j] = 1
                    q.append(((i, j), 0))

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        while q:
            (r, c), s = q.popleft()
            res[r][c] = s

            for i in range(4):
                nr, nc = r + drow[i], c + dcol[i]
                if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0:
                    vis[nr][nc] = 1
                    q.append(((nr, nc), s + 1))

        return res
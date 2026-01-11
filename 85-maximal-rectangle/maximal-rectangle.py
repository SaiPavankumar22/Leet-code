class Solution:
    def largestRectangleArea(self, heights):
        st = []
        n = len(heights)
        left_small = [0] * n
        right_small = [0] * n

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if not st:
                left_small[i] = 0
            else:
                left_small[i] = st[-1] + 1
            st.append(i)

        while st:
            st.pop()

        for j in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[j]:
                st.pop()
            if not st:
                right_small[j] = n - 1
            else:
                right_small[j] = st[-1] - 1
            st.append(j)

        max_area = 0
        for k in range(n):
            wi = right_small[k] - left_small[k] + 1
            max_area = max(max_area, heights[k] * wi)

        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        max_area = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            area = self.largestRectangleArea(heights)
            max_area = max(max_area, area)

        return max_area
        
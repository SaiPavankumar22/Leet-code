# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
        lis = []
        def recur(node):
            if(not node):
                return
            lis.append(node.val)
            recur(node.left)
            recur(node.right)
        recur(root)
        k = Counter(lis)
        m = 0
        for i in lis:
             m = max(m,k[i])
        res = []
        for j in lis:
            if(k[j]==m):
                res.append(j)
        return list(set(res))

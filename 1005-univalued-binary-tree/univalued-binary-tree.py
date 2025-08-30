# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        res = []
        def roots(node):
            if node:
                res.append(node.val)
                roots(node.left)
                roots(node.right)
        roots(root)
        k = set(res)
        if(len(k)==1):
            return True
        else:
            return False
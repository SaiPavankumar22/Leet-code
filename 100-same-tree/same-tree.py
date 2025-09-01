# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def chk(p,q):
            if((p is None) and (q is None)):
                return True
            if((p is None) or (q is None)):
                return False
            if(p.val == q.val):
                return chk(p.left,q.left) and chk(p.right,q.right) 
            else:
                return False
        return chk(p,q)
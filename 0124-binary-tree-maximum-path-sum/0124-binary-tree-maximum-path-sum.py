# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def getSum(self,root):
        if root is None:
            return 0
        left = max(0,self.getSum(root.left))
        right = max(0,self.getSum(root.right))
        self.ans = max(root.val+left+right,self.ans)
        return root.val+max(left,right)
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = float('-inf')
        self.getSum(root)
        return self.ans
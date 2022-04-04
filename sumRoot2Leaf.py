# RECURSIVE SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0
        self.dfs(root,0)
        return ans
    
    def dfs(self, root, val):
        global ans
        if(root == None):
            return False
        
        val = (val * 10) + root.val
        
        if(root.left == None and root.right == None):
            ans = ans + val
            return
        
        self.dfs(root.left, val)
        self.dfs(root.right, val)
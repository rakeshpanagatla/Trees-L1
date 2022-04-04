# DFS using stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, targetSum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
        return res
                

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, targetSum, result, [])
        return result
        
    def dfs(self, root, targetSum, result, path):
        if not root:
            return
        
        path.append(root.val)
        
        if root.left == None and root.right == None:
            if not targetSum - root.val:
                result.append(path[:])
                
        else:
            self.dfs(root.left, targetSum - root.val, result, path)
            self.dfs(root.right, targetSum - root.val, result, path)
                
#         BACKTRACK
        path.pop()
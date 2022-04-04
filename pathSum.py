# DFS using stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while(stack):
            curr, value = stack.pop()
            if(curr.right == None and curr.left == None and value == targetSum):
                return True
            if curr.left:
                stack.append((curr.left, value + curr.left.val))
                
            if curr.right:
                stack.append((curr.right, value + curr.right.val))
        return False    


# recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(not root):
            return False
        if(root.left == None and root.right == None and root.val == targetSum):
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right,targetSum - root.val)
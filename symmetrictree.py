# ITERATIVE SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while(stack):
            right = stack.pop()
            left = stack.pop()
            if(left == None and right == None):
                continue
            if(left == None or right == None):
                return False
            if(left.val != right.val):
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

# recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if(root == None):
            return False
        return self.helper(root.left, root.right)
        
    def helper(self, left: [TreeNode], right: [TreeNode]):
        if(left == None and right == None):
            return True
        if(left == None or right == None):
            return False
        if(left.val != right.val):
            return False
        
        outside = bool(self.helper(left.left, right.right))
        inside = bool(self.helper(left.right, right.left))
        
        return inside and outside
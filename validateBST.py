# RECURSIVE SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
prev = None
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global prev
        prev = None
        return(self.in_order(root))
    
    
    def in_order(self, root):
        global prev
        if(root is None):
            return True
        leftresult = bool(self.in_order(root.left))
        if (leftresult == False):
            return False
        
        
        if(prev is not None and prev.val>=root.val):
            return False
        prev = root
        return self.in_order(root.right)

# NON RECURSIVE SOLUTION/ ITERATIVE SOLUTION
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        #         checking whether root is null or stack is empty(stack becomes empty when we come back to root node in in-order traversal)
        while(root or stack):
#         making sure root status again as the above loop might pass if stack is empty
#  Left edges
            while(root):
                stack.append(root)
                root = root.left

#                 Node operation
            root = stack.pop()
            
#     checking if root is less than equal to prev(returning false)         
            if(prev and prev.val>=root.val):
                return False
            
            prev = root
#             Right edges
            root = root.right

        
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Effiecient Solution


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        global p 
        p = 0
        hashmap = dict()
        if(len(preorder) == 1):
            return TreeNode(preorder[0])
        for i in range(0, len(inorder)):
            hashmap[inorder[i]] = i
            
        return self.helper(preorder, 0, len(preorder) - 1, hashmap)
    
    def helper(self, preorder, start, end, hashmap):
        global p
            
        
        
        if(start > end or p == len(preorder)):
            return None
        
        inorderIndex = hashmap.get(preorder[p])
        root = TreeNode(preorder[p])
        
        p += 1
        
        root.left = self.helper(preorder, start, inorderIndex - 1, hashmap)
        root.right = self.helper(preorder, inorderIndex + 1, end, hashmap)
        
        return root
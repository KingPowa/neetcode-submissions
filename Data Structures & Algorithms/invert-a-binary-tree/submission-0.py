# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node: Optional[TreeNode]):
            if node is None:
                # Empty root
                return node
            elif node.left is None and node.right is None:
                # Leaf
                return node
            
            node.left = invert(node.left)
            node.right = invert(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp
            return node

        return invert(root)
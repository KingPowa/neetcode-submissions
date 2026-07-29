# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def sameTree(self, root1, root2):
        if (root1 is None and root2 is not None) or \
            (root1 is not None and root2 is None):
            return False

        if not root1 and not root2: return True
        if root1.val == root2.val: 
            if self.sameTree(root1.left, root2.left):
                return self.sameTree(root1.right, root2.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not self.sameTree(root, subRoot):
            if root is not None:
                if not self.isSubtree(root.left, subRoot):
                    return self.isSubtree(root.right, subRoot)
            else:
                return False
        return True

        

        

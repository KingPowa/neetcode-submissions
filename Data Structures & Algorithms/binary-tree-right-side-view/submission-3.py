# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rightSideViewRecurs(node, depth):
            if node is None:
                return
            else: 
                while depth >= len(res):
                    res.append(node.val)

            right_rightSideView = rightSideViewRecurs(node.right, depth + 1)
            left_rightSideView = rightSideViewRecurs(node.left, depth + 1)
        
        rightSideViewRecurs(root, 0)
        return res
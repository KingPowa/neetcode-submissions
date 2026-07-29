# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        
        lo = [[root.val]]
        # Assume levelOrder returns it
        lo_left = self.levelOrder(root.left)
        lo_right = self.levelOrder(root.right)
        # Will be in format of level
        lo_l_left = len(lo_left)
        lo_l_right = len(lo_right)
        if lo_l_left > lo_l_right:
            for i in range(lo_l_left):
                lp = lo_left[i]
                if i < lo_l_right:
                    lp.extend(lo_right[i])
                lo.append(lp)
        else:
            for i in range(lo_l_right):
                lp = []
                if i < lo_l_left:
                    lp.extend(lo_left[i])
                lp.extend(lo_right[i])
                lo.append(lp)
        print(lo)
        return lo

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        track = []
        while root or track:
            while root:
                track.append(root)
                root = root.left
            root = track.pop()
            out.append(root.val)
            root = root.right
        return out
            
        
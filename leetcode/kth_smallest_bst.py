from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        # inOrder
        def helper(self, root):
            if not root:
                return
            helper(self, root.left)
            res.append(root.val)
            helper(self, root.right)

        helper(self, root)

        return res[k-1]

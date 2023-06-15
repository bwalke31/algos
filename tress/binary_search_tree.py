class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def search(root, target):
    if root is None:
        return False
    if target < root.val:
        search(root.left, target)
    elif target > root.val:
        search(root.right, target)
    else:
        return True

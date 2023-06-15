from tree_node import TreeNode


# The smaller value will always be on the left
def getMin(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


# Can insert and remove in logn time (assuming roughly balanced)
# This is an advantage over inserting and removing with sorted arrays (n time)
def insert(root, val):
    # Empty tree
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        return root


# Two cases:
# Case 1: 0 or 1 child
# Case 2: 2 children
# In the case of 2 children, we want to replace it with the smallest leafnode in the right subtree
# This is because it will be greater than all the values in the left subtree and satisfy BT conditions
def remove(root, val):
    if not root:
        return None
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    # Once we've reached the desired node...
    else:
        # Cases for one child
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        # Cases for two children
        else:
            # Get the min node of right subtree
            minNode = getMin(root.right)
            # Assign the current root value that value
            root.val = minNode.val
            # Remove the min node
            root.right = remove(root.right, minNode.val)
    return root

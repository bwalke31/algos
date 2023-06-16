from tree_node import TreeNode

'''
Time complexity: O(n) => We must visit every node in the
tree since we are printing, in this example, in order.

If we are given random values and need to sort them using a BST,
the time complexity will be O(n + nlogn) => O(nlogn) since nlogn
dominates. We first have to insert each value into the tree (nlogn), then
visit every node (n)
'''


def inOrder(root):
    # Base case for null
    if not root:
        return
    # Want to process the left subtree first since
    # we know it will have a smaller value
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


'''
Preordering is printing the root, the entire left subtree, then the entire right
subtree
'''


def preOrder(root):
    # Base case for null
    if not root:
        return
    print(root.val)
    inOrder(root.left)
    inOrder(root.right)


'''
Postorder works by printing all the values in the left subtree, all the values in
the right subtree, and then finally the root
'''


def postOrder(root):
    # Base case for null
    if not root:
        return
    inOrder(root.left)
    inOrder(root.right)
    print(root.val)

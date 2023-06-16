from collections import deque

'''
Want to go through each layer of the tree (typically left to right).
Time Complexity: O(3N) => O(n)
    - We visit each node, add it to the queue, and then pop it from the queue; 3 operations
    - Don't get confused with nested loops!!
'''


def bfs(root):
    queue = deque()

    if (root):
        deque.append(root)

    level = 0
    while len(queue) > 0:
        print('level: ', level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1

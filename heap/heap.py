
'''
    left child = 2 * i
    right child = 2 * i + 1
    parent = i / 2
'''

# Min heap


class heap:
    def __init__(self) -> None:
        self.heap = [0]

    '''
        1. Append the value and get position
        2. While idx is greater than one and less than the parent continue to swap
        Time Complexity: O(logn)
    '''

    def push(self, val):
        self.heap.append(val)
        idx = len(self.heap) - 1

        while idx > 1 and self.heap[idx] < self.heap[idx // 2]:
            tmp = self.heap[idx]
            self.heap[idx] = self.heap[idx // 2]
            self.heap[idx // 2] = tmp
            idx = idx // 2

    '''
        1. Check to see if heap is empty or if one element 
        2. If more than one element, move the last value to the root
        3. Compare right and left nodes
        4. Swap with the smaller node if the current node is larger
        5. Continue this process until a condition is not met
        Time Complexity: O(logn)
    '''

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        # Move last value to root
        self.heap[1] = self.heap.pop()
        # idx 1 is the first node since there's a dummy node
        i = 1
        # Percolate down
        # Checking to make sure there's a left child
        while 2 * i < len(self.heap):
            # Checking to see if there's a right child
            if (2 * i + 1 < len(self.heap) and
                # If the right child is smaller than the left...
                self.heap[2 * i + 1] < self.heap[2 * i] and
                    # ...and if the current node is greater than the right child
                    self.heap[i] > self.heap[2 * i + 1]):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

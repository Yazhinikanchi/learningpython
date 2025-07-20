from queue import Queue

# Create a queue
q = Queue()

# Enqueue elements
q.put("F")
q.put("B")
q.put("D")

# Dequeue elements
print(q.get())  # Output: A (FIFO)
print(q.get())  # Output: B


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

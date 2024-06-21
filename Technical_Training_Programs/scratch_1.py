class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def topview(root):
    if root is None:
        return

    q = []
    m = dict()

    # Initialize horizontal distance of root
    hd = 0
    q.append((root, hd))

    while len(q):
        node, hd = q.pop(0)

        # If a node with the same horizontal distance is not already in the map
        if hd not in m:
            m[hd] = node.data

        if node.left:
            q.append((node.left, hd - 1))

        if node.right:
            q.append((node.right, hd + 1))

    # Print the top view from leftmost to rightmost
    for key in sorted(m):
        print(m[key], end=" ")


# Example usage
# Construct a binary tree
#         1
#       /   \
#      2     3
#       \   / \
#        4 5   6
#           \
#            7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)

topview(root)

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

# preorder_travesal( left - root - right)

def postorder(node):

    # base case
    if node == None:
        return
    
    postorder(node.left) # go to left , go to right , then print the data
    postorder(node.right)
    print(node.data)


if __name__ == "__main__":
# Create the root node
    root = Node(1)

# Create the left subtree
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)

# Create the right subtree
    root.right = Node(3)
    root.right.right = Node(6) # Note: The left child of 3 is None

# --- Test your function ---
    print("Preorder Traversal:")
    postorder(root)

'''
      1
     / \
    2   3
   / \   \
  4   5   6
'''
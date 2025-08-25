class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

# preorder_travesal( left - root - right)

def inorder(node):

    # base case
    if node == None:
        return
    
    inorder(node.left) # go to left print left while comming back to right print root
    print(node.data)
    inorder(node.right)


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
    inorder(root)

'''
      1
     / \
    2   3
   / \   \
  4   5   6
'''

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


def postorder(node):
    stack1=  []
    stack2 = []
    stack1.append(node)
    while(stack1):
        element = stack1.pop()
        stack2.append(element.data)
        if element.left is not None:
            stack1.append(element.left)
        if element.right is not None:
            stack1.append(element.right)
    return stack2[::-1] # we should return in revrse order



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
    print(postorder(root))

'''
      1
     / \
    2   3
   / \   \
  4   5   6
  '''
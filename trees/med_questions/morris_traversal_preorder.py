class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
def morris(root):
    preorder = []
    curr = root
    while curr:
        if curr.left is None:
            preorder.append(curr.val)
            curr = curr.right # go right as left is null
        else:
            # if left is not empty
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right # go to the rightest most node
            if prev.right is None:
                # we reached a leaf node i guess
                prev.right = curr # make a thread to the current
                preorder.append(curr.val)
                # as right is empty go left
                curr = curr.left
            else:
                # if thread exist remove it
                prev.right = None
                curr = curr.right
    return preorder

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
print(morris(root))
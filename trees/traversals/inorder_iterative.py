def inorder(root):
    ans = []
    stack = []
    node = root
    stack.append(root)
    while(True):
        if node is not None:
            stack.append(node)
            nde = node.left
        else:
            if stack:
                break
            node = stack.pop()
            ans.append(node)
            node = node.right
    return ans
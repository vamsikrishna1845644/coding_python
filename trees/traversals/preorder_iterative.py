def preorder(root):
    ans = [] # to store the ans
    stack = []
    if root is None:
        return ans
    stack.append(root)
    while(stack):
        element = stack.pop()
        ans.append(element)
        if element.right is not None:
            stack.append(element.right)
        if element.left is not None:
            stack.append(element.left)
    return ans
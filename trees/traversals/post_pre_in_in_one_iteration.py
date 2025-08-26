def post_pre_in(root):
    if root is None:
        return [] , [] , []
    stack = [] # our stack to keep a check
    pre = [ ]
    post = []
    in_ = [] 
    
    stack.append((root,1))
    while stack:
        top = stack.pop()

        # means preorder
        if top[1] == 1:
            pre.append(top[0].val)
            top[1] += 1
            stack.append(top)
            # if its left is not null
            if top[0].left is not None:
                stack.append((top[0].left,1))
        elif top[1] == 2:
            in_.append(top[0].val)
            top[1] += 1
            stack.append(top)
            # if its right is not null
            if top[0].right is not None:
                stack.append((top[0].right,1))
        else:
            # add to the post order
            post.append(top[0].val)
    return pre ,in_ ,post
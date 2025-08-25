def postorder(root):
    stack = []
    ans = [] # for returning the ans
    if root == None:
       return []
    curr = root
    while curr or stack:
         #  Keep going left, pushing nodes to the stack
        if curr :
             stack.append(curr)
             curr = curr.left
        else :
            # look at the right child of the element in the top of the stack
            temp = stack[-1].right

            if not temp :
                # if no right child 
                # pop the elemnt and push to our ans list
                temp = stack.pop()
                ans.append(temp.val)
                # we pop while the last popped node is the right child of the stack’s top (meaning both left and right subtrees are done).
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    ans.append(temp.val)
            else:
                # there is a right child 
                # process it set curr to it
                curr = temp
    return ans

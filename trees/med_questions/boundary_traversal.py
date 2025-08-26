def isleaf(node):
     if node is not None and node.left is None and node.right is None:
          return True
     else:
          return False

def addleafnodes(node,ans):
        if node is None:
            return 
        if isleaf(node):
            ans.append(node.val)
            return
        addleafnodes(node.left,ans)
        addleafnodes(node.right,ans)
def left_boundary(root,ans):
     curr = root.left
     while curr:
          if not isleaf(curr):
                ans.append(curr.val)
          if curr.left:
               curr = curr.left
          else:
               curr = curr.right
def right_boundary(root,temp):
     curr = root.right
     while curr:
          if not isleaf(curr):
                temp.append(curr.val)
          if curr.right:
               curr = curr.right
          else:
               curr = curr.left
def boundary_traversal(root):
    if root is None or  isleaf(root):
        return []
    temp = []
    ans= [ ] # answer
    ans.append(root.val)
    left_boundary(root, ans)
    addleafnodes(root,ans)
    right_boundary(root,temp)
    for i in reversed(temp):
         ans.append(i)
    return ans
   
    
class Solution:
    # doing this in morris traversal
    # for recursive way look at pseudo code in the book
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right # make a thread
                curr.right = curr.left 
                curr.left = None
            curr = curr.right
        return root
    

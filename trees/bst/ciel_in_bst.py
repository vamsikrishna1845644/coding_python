class Solution:
    def floorCeilOfBST(self, root, key):
        ciel = [-1] # a list to pass by refernce
        self.recursive(root,key,ciel):
        return ciel[0]
    def recursive(self , node , key , ceil):
        # base case
        if node is None:
            return 
        
        if node.val == key:
            ceil[0] = node.val
            return
        if node.val > key:
            ceil[0] = node.val
            return self.recursive(node.left , key ,ceil)
        if node.val < key:
            return self.recursive(node.right , key ,ceil)
        

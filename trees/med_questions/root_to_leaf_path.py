class Solution:
    def allRootToLeaf(self, root):
        ans = [ ] # to store all the paths and return the ans
        temp = [] #temporary array
        self.recursive(root , ans ,temp)
        return ans
    def recursive(self,node,ans,temp):
        if node is None:
            return
        temp.append(node.data)  # add it 
        if node.left is None and node.right is None:
            ans.append(temp[:]) # copy of the temp 
        self.recursive(node.left , ans ,temp)
        self.recursive(node.right , ans ,temp)
        temp.pop() # back track
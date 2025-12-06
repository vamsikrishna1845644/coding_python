class Solution:
    def dfsOfGraph(self, V, adj):
        vis = [0]*V # visisted array
        dfs = [] # to store answerr
        start = 0
        self.dfs(start,vis,adj,dfs)
        return dfs
    def dfs(self,node,vis,adj,dfs):
        # when it comes to this function
        vis[node] = 1 # mark as visted
        dfs.append(node) # add the node to answer

        for i in adj[node]: # iterate for each neighbour to that node

            # if that neigbiur is not visited
            if not vis[i]:
                self.dfs(i,vis,adj,dfs) # go to the depth of that neighbour

        

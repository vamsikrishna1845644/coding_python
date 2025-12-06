class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # we have been given a adjnacency matrix
        #as we are family with traverslas on adj list
        # convert this into adj list
        n = len(isConnected)
        count = 0 
        adj = [[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):

                if isConnected[i][j] == 1 and i != j: # same element should not be taken (i.e i,i)
                    adj[i].append(j)
                    adj[j].append(i) # as both are nieghbours to each other
        vis = [0] * n # visited array
        for i in range(n):
            if not vis[i]:
                # if this is not vsited
                # increase the count and call the dfs as its the starting node of a province
                count += 1
                self.dfs(i,adj,vis)
        return count
    def dfs(self,node,adj,vis):
        # mark that node as visited
        vis[node] = 1
        for i in adj[node]: # for each of its neigh bour
            if not vis[i]: # if they are not vsited
                self.dfs(i,adj,vis) # go to their depths
        


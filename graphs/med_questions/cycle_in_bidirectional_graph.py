class Solution:
    def isCyclic(self, N, adj):
        # using dfs
        #Initialize a visited array
        vis = [0]*N
        # initialize a path array to store the path traversed
        path= [0]*N

        # to not miss anything we have to do a connected components logic
        for i in range(N):
            # if not visited
            if not vis[i]:
                # do the dfs
                if self.dfs(i,adj,vis,path): # if cycle is presnt true should be returned
                    return True
        return False
    def dfs(self,node,adj,vis,path):
        # mark as visited
        vis[node] = 1
        # add to our path 
        path[node] = 1

        # travers the nodes neighbours
        for neighbour in adj[node]:
            if not vis[neighbour] : # noot vsiietd and not in path
                # call the next dfs
                if self.dfs(neighbour,adj,vis,path):
                    return True
            if path[neighbour]: # if again came in path
                return True # cycle exists
        path[node] = 0 # backtrack
        return False
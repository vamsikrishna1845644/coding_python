class Solution:
    def dfs(self,vis,adj,node,st):
        # mark as vis
        vis[node] = 1

        # for each of its neighbours
        for neighbour in adj[node]:
            # if thet are nnot vsited 
            # go to the depths of them
            if not vis[neighbour]:
                self.dfs(vis,adj,neighbour,st)
            
        # when dfs ends
        # push top stack
        st.append(node)


    def topoSort(self, V, adj):
       
       #declare the vis array 
       vis = [0]*V
       # decalre the stack
       st = []
       # for all non vis elements call dfs
       for i in range(len(vis)):
           if not vis[i]:
               # call the dfs
               self.dfs(vis,adj,i,st)

       return st[::-1]



           

from collections import deque
class Solution:
    def isCycle(self, V, adj):
        vis = [0]*V # visisted array
        # assuming connected componets
        for i in range(len(vis)):
            if not vis[i]:
              if self.detect(i,adj,vis,-1) == True:
                  return True
        return False
    def detect(self,node,adj,vis,parent):
        # mark the node as visited
        vis[node] = 1
        q = deque()
        q.append([node,parent])

        while q:
            n , p = q.popleft()
            # iterate through all the neighbour for that node and add them to queue
            for i in adj[n]:
                # to the queue if not vsisted
                if not vis[i]:
                    # mark as visited
                    vis[i] = 1
                    q.append([i,n]) # i -> node , n ->parent
                elif i != p: # if the neigbour is not its parent
                    # we know its has a loop now as it was visted by someone other than parent
                    return True
        return False

edges = [[0, 1], [0, 2], [2, 3]]
V = 4
adj = [[] for _ in range(V)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
sol =Solution()
print(sol.isCycle(V,adj))
        
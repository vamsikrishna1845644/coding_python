from collections import deque
class Solution:
    def topoSort(self, V, adj):
        # decalre indegree list
        indegree = [0]*V
        # decalre our queue
        q = deque()
        # declare our ans
        ans = []
        # populate/ fill the indegree list
        # traverse the adj list
        for node in range(V):
            for neighbour in adj[node]:
                # increase the indegree of all thye neighbours by 1 
                #as they have 1 degree from the node
                indegree[neighbour]+=1
        # now we have indegree list
        # lets   use bfs to traverse all the elements connected to zero in degree elemts and minus there indegree
        # now we check again if indegree of any  element is zero if yes , we add that element to our queue
        for node  in range(V):
            if indegree[node] == 0:
               # add them to our queue
               q.append(node)
        # now we have our queue populated lest ise bfs algo 
        while  q:
            ele = q.popleft()
            # add to our ans
            ans.append(ele)
            # for this element minus all its connected nodews by 1
            for neigbour in adj[ele]:
                    indegree[neigbour]-=1
                    if indegree[neigbour]==0:
                        # append to our queue
                        q.append(neigbour)
        return ans
V = 6
adj = [
    [2, 3],  # 0 → 2, 3
    [3, 4],  # 1 → 3, 4
    [3],     # 2 → 3
    [5],     # 3 → 5
    [],      # 4 → (no outgoing edges)
    []       # 5 → (no outgoing edges)
]

sol = Solution()
print(sol.topoSort(V, adj))
                




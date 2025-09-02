from collections import deque
class Solution:
    def bfsOfGraph(self, V, adj):
        # v is number of nodes
        # adj is the adjnacency matrix
        # create a vsisted array
        vis = [0]*V
        vis[0] = 1 # for 1 based indexing
        bfs = [] # to store the answer
        q = deque() # for bfs traversal
        q.append(0) # add the first node
        while q:
            curr = q.popleft()
            # add to the answer
            bfs.append(curr)
            # add the neighbours of current to the queue
            for i in adj[curr]:
                if not vis[i]: # to check if already visisted
                    # make the neighbours as visited
                    vis[i] = 1
                    q.append(i)
        return bfs

if __name__ == "__main__":
    V = 10
    adj = [
        [1, 2, 3],      # 0 connected to 1, 2, 3
        [0, 4, 5],      # 1 connected to 0, 4, 5
        [0, 6],         # 2 connected to 0, 6
        [0, 7],         # 3 connected to 0, 7
        [1, 8],         # 4 connected to 1, 8
        [1, 9],         # 5 connected to 1, 9
        [2, 7, 8],      # 6 connected to 2, 7, 8
        [3, 6, 9],      # 7 connected to 3, 6, 9
        [4, 6],         # 8 connected to 4, 6
        [5, 7]          # 9 connected to 5, 7
    ]
    sol = Solution()
    print(sol.bfsOfGraph(V,adj))

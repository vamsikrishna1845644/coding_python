from collections import deque
class Solution:
    def findNumberOfComponent(self, V, edges):
        # doing this using bfs and adjaency matrix
        n = len(edges) # rows
        m = len(edges[0]) # cols
        vis = [[0]*m for _ in range(n)] # initialize the visited matrix
        count = 0
        for i in range(n):
            for j in range(m):
                # iterate for each element in the matrix
                if not vis[i][j] and edges[i][j] == 1:
                    self.bfs(i,j,edges,vis) # ( roe,col,adj,vis)
                    count += 1 # increase the count
        return count
    def bfs(self,row,col,edges,vis):
        # mark the element as visited
        vis[row][col] = 1
        q = deque()
        q.append([row,col])
        n = len(edges) # rows
        m = len(edges[0]) # cols
        while q:
            i,j = q.popleft()

            # check the neighbours and add them to queue
            # as theere are neighbours in 8 directions
            for delr in [-1,0,1]:
                for delc in [-1,0,1]:
                    newr = i + delr # newr -> newrow amd delr -> deltarow
                    newc = j + delc # similarly
                    # verify if newc and newr exists inside the matrix , they are not visted and they are land(i.e 1)
                    if newr>=0 and newr < n and newc >=0 and newc < m and not vis[newr][newc] and edges[newr][newc] == 1:
                        # add them to the  stack
                        q.append([newr,newc])
                        # mark them as visited
                        vis[newr][newc] = 1

edges = [
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0]
]

sol = Solution()
print(sol.findNumberOfComponent(4, edges))
    
       
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # solving this using bfs
        V = len(graph)
        color = [-1]*V
        # color = 0 , 1
        for i in range(V):
            if color[i] == -1:
                if self.bfs(i,graph,color) == False:
                    return False
        return True
    def bfs(self,first,graph,color):
        q = deque()
        q.append(first) # the first elemet in graph
        # colour it
        color[first] = 0 # staring colour is 0 # even not connected

        while q:
            node = q.popleft()
            # check for its neigbours
            for neighbour in graph[node]:
                if color[neighbour] == -1 and color[node] == 0:
                    # colur it will  1
                    color[neighbour] = 1
                    # add the neighbout to queue
                    q.append(neighbour)
                elif  color[neighbour] == -1 and color[node] == 1:
                    # colur it will  0
                    color[neighbour] = 0
                    # add the neighbout to queue
                    q.append(neighbour)
                elif color[neighbour] == color[node]:
                    return False
        return True
class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # solving using dfs
        V = len(graph)
        color = [-1]*V

        # componets
        for i in range(V):
            if color[i] == -1:
                # its not colored call dfs with color 0
                if self.dfs(i,0,graph,color) == False:
                    return False
        return True
    def dfs(self,node,col,graph,color):
        # fiest set  its  color
        color[node] = col
        # call  dfs for its neighbours
        for neighbour in graph[node]:
            if color[neighbour] == -1: # not coloured
                if color[node] == 0:
                    if not self.dfs(neighbour,1,graph,color): # call dfs with  opp colour
                        return False 
                if color[node] == 1:
                    if not self.dfs(neighbour,0,graph,color): # call dfs with  opp colour
                        return False 
            elif color[neighbour] == color[node]: # same color
                return False
        return True

from collections import deque

class Solution:
    def shortestPath(self, edges, N, M):
        """
        Find the shortest path from source node 0 to all other nodes
        in an undirected, unweighted graph.
        
        Parameters:
        edges: List of edges where each edge is [u, v]
        N: Number of vertices (0 to N-1)
        M: Number of edges
        
        Returns:
        List of shortest distances from node 0 to each node. 
        If a node is unreachable, distance is -1.
        """

        # Step 1: Convert edge list into adjacency list
        adj = [[] for _ in range(N)]
        for i in range(M):
            u, v = edges[i]
            adj[u].append(v)
            adj[v].append(u)  # because the graph is undirected

        # Step 2: Initialize distances with infinity
        distance = [float('inf')] * N

        # Step 3: Initialize BFS queue
        q = deque()

        # Distance of source node (0) to itself is 0
        distance[0] = 0
        q.append(0)

        # Step 4: Perform BFS to calculate shortest distance
        while q:
            node = q.popleft()
            for neighbour in adj[node]:
                # If a shorter path to neighbour is found
                if distance[node] + 1 < distance[neighbour]:
                    distance[neighbour] = distance[node] + 1
                    q.append(neighbour)

        # Step 5: Replace unreachable nodes' distance with -1
        for i in range(N):
            if distance[i] == float('inf'):
                distance[i] = -1

        return distance

         

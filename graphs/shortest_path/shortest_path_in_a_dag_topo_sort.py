class Solution:
    def dfs(self, vis, adj, topo, node):
        """
        DFS for topological sorting using post-order traversal.
        A node is added to topo after all its descendants are processed.
        """
        vis[node] = True
        for neighbour, weight in adj[node]:
            if not vis[neighbour]:
                self.dfs(vis, adj, topo, neighbour)
        topo.append(node)

    def shortestPath(self, edges, N, M):
        """
        Find shortest path from source node 0 to all other nodes in a DAG.
        Returns: distance array where distance[i] = shortest distance from 0 to i, 
                 or -1 if unreachable from 0
        """
        
        # Build adjacency list: adj[u] = [(v, weight), ...]
        adj = [[] for _ in range(N)]
        
        for u, v, w in edges:
            adj[u].append((v, w))

        # Step 1: Topological Sort using DFS
        # This sorts ALL nodes in topological order
        vis = [False] * N
        topo = []
        
        for node in range(N):
            if not vis[node]:
                self.dfs(vis, adj, topo, node)
        
        # topo is in reverse topological order, so reverse it
        topo.reverse()

        # Step 2: Initialize distances
        # Source node (0) has distance 0
        # All other nodes start with -1 (unreachable)
        distance = [-1] * N
        distance[0] = 0

        # Step 3: Relax edges in topological order
        # Process nodes in topological order and update distances to neighbors
        for u in topo:
            # Only process if u is reachable from source 0 (distance != -1)
            if distance[u] != -1:
                for v, w in adj[u]:
                    # If v is unreachable, set distance
                    # Otherwise, update with minimum distance
                    if distance[v] == -1:
                        distance[v] = distance[u] + w
                    else:
                        distance[v] = min(distance[v], distance[u] + w)

        return distance



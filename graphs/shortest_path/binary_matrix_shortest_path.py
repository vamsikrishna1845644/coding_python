from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # We are allowed to move in 8 directions
        # Only cells with value 0 can be traversed
        # Our goal: find the shortest path length from top-left (0,0)
        # to bottom-right (n-1, m-1)
        
        # Base condition: if the starting cell is blocked (1), no path exists
        if grid[0][0] == 1:
            return -1

        # Step 1: Initialize basic parameters
        n = len(grid)
        m = len(grid[0])
        
        # Step 2: Create a 2D distance matrix initialized with infinity
        # dist[r][c] stores the shortest distance to reach cell (r, c)
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        
        # Distance of source node (0,0) is 0
        dist[0][0] = 0

        # Step 3: Initialize queue for BFS (we use deque for O(1) pop/append)
        # Each element: [current_distance, (row, col)]
        q = deque()
        q.append([0, (0, 0)])

        # Step 4: Perform BFS traversal
        while q:
            # Pop the front element from the queue
            distance, cordinates = q.popleft()
            Row = cordinates[0]
            Col = cordinates[1]

            # Step 5: Define 8 possible directions (row and column deltas)
            delr = [1, -1, -1, 1, 0, 1, -1, 0]
            delc = [1, -1, 1, -1, 1, 0, 0, -1]

            # Step 6: Traverse all 8 neighboring cells
            for i in range(8):
                row = delr[i] + Row
                col = delc[i] + Col

                # Step 7: Check boundary conditions
                if (row >= 0 and row < n) and (col >= 0 and col < m):
                    # Step 8: Proceed only if the cell is unblocked (0)
                    # and a shorter path is found for this neighbor
                    if grid[row][col] == 0 and distance + 1 < dist[row][col]:
                        # Update the shortest distance for neighbor
                        dist[row][col] = distance + 1
                        # Push this neighbor into the queue for further exploration
                        q.append([distance + 1, (row, col)])

        # Step 9: After BFS, check if destination (n-1, m-1) is reachable
        if dist[n-1][m-1] == float('inf'):
            # Destination not reachable
            return -1
        else:
            # +1 because path length counts the starting cell as well
            return dist[n-1][m-1] + 1




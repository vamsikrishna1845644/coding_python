import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        if n == 1 and m == 1:
            return 0  # single cell → no effort needed

        # Distance matrix (stores min effort to reach each cell)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        # Min-heap -> (effort_so_far, row, col)
        pq = [(0, 0, 0)]
        delr = [0, -1, 0, 1]
        delc = [-1, 0, 1, 0]

        while pq:
            difference, Row, Col = heapq.heappop(pq)


            # If reached destination, return the minimum effort
            if Row == n - 1 and Col == m - 1:
                return difference

            # Explore all 4 directions
            for i in range(4):
                row, col = Row + delr[i], Col + delc[i]
                if 0 <= row < n and 0 <= col < m:
                    # Effort of this move = max of current effort and height diff
                    neweffort = max(difference, abs(heights[row][col] - heights[Row][Col]))
                    if neweffort < dist[row][col]:
                        dist[row][col] = neweffort
                        heapq.heappush(pq, (neweffort, row, col))

        # Return effort to reach bottom-right cell
        return dist[n - 1][m - 1]

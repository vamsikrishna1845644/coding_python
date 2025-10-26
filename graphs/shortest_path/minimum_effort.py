import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # trying this question
        # without comments
        n = len(heights)
        m  = len(heights[0])
        if n == 1 and m == 1:
            return 0
        dist  = [[float('inf')]*m for _ in range(n)]

        pq = []
        # instead of path lenght 
        # lets try storing the absolute diff
        heapq.heappush(pq,(0,0,0))

        while pq:
            difference , Row,Col = heapq.heappop(pq)

            # check if 4 directions
            delr = [0,-1,0,1]
            delc = [-1,0,1,0]
            for i in range(4):
                row = delr[i] + Row
                col = delc[i] + Col

                if 0<= row < n and 0 <= col < m :
                    neweffort = max(abs(heights[row][col] - heights[Row][Col]),difference)
                    if neweffort < dist[row][col]:
                        # push to the pq
                        heapq.heappush(pq,(neweffort,row,col))
                        dist[row][col] = neweffort


        return dist[n-1][m-1]
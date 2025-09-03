from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # lets use bfs
        n = len(image) # this is simalr to before so not writing commits just do it
        m = len(image[0])

        vis = [[0]*m for _ in range(n)]
        rangu = image[sr][sc]
        self.bfs(sr,sc,image,vis,color,rangu)
        return image
    def bfs(self,row,col,image,vis,color,rangu):
        n = len(image) # this is simalr to before so not writing commits just do it
        m = len(image[0])
        # mark this as visted
        vis[row][col] = 1
        # change its rangu
        image[row][col] = color
        q = deque()
        q.append([row,col])
        while q:
            r,c = q.popleft()

            # check for all neighbours only in 4 directions and add them to queue and change their rangu to color
            for delr in [-1,0,1]:
                for delc in [-1,0,1]:
                    # we need only 4 directions
                    if (delr == 0 and ( delc == 1 or delc == -1)) or (delc == 0 and (delr == 1 or delr == -1)):
                        newr = r + delr
                        newc = c + delc
                        if newr>=0 and newr< n and newc >=0 and newc<m and not vis[newr][newc] and image[newr][newc] == rangu:
                            # mark as visited 
                            vis[newr][newc] = 1
                            # chnage its rangu to color
                            image[newr][newc] = color
                            q.append([newr,newc])

                    

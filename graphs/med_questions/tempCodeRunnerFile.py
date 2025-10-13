from collections import deque
class Solution:
    def isCyclic(self, N, adj):
        # doing this using kahns algorithm
        # we use kahns algo if the ans returns N elements -> no cycle
        #  if the ans returns <N elements ->  cycle exists
        indegree = [0]*N

        # ans
        ans = []
        # queue
        q = deque()

        # populated the indegree list 
        for node in range (N):
            for neighbour in adj[node]:
                # increse the indegree of neighbour by 1
                indegree[neighbour]+=1
        
        # now we have a popualted indegree , check for elements having indgree = 0
        # and add those elements into our queue
        for node in range(N):
            if indegree[node] == 0:
                # add to the queue
                q.append(node)
        
        # bfs algo
        while q:
            ele = q.popleft()
            #add the elemnt to our ans
            ans.append(ele)

            # decrease all the ele's neigbours indegree by 1
            for neighbour in adj[ele]:
                indegree[neighbour] -=1
                # if again indegree is zero 
                if indegree[neighbour] ==0:
                    #add them to our queue
                    q.append(neighbour)
        # checking condition
        if len(ans) == N:
            return True
        else:
            return False
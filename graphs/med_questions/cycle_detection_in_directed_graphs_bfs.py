from collections import deque
class Solution:
    def isCyclic(self, N, adj):
        # doing this using kahns algorithm
        # we use kahns algo if the ans returns N elements -> no cycle
        #  if the ans returns <N elements ->  cycle exists
        indegree = [0]*N

        # ans
        count =0
        # no need to store entire ans jus count is enough
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
            #increase the count by 1 instead of adding the element (waste of space)
            count+=1

            # decrease all the ele's neigbours indegree by 1
            for neighbour in adj[ele]:
                indegree[neighbour] -=1
                # if again indegree is zero 
                if indegree[neighbour] ==0:
                    #add them to our queue
                    q.append(neighbour)
        # checking condition
        if count == N:
            return False # nocycle
        else:
            return True # cycle exists

V = 6
adj= [ [1], [2, 5], [3], [4], [1], [ ] ]
sol = Solution()
print(sol.isCyclic(V,adj))
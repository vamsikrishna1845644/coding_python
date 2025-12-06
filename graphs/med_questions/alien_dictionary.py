from collections import deque
class Solution:
    def findOrder(self, dict, N, K):
       # this is a question where we need to use the topo sort
       #but to get to there first we need to built the graph ( ie. the adj list)
       # N is the no  of words in dict and k is the no of starting words
       # here in our graphs k is the no of nodes
       # for k letters ( a , b , c ,d .....) as u know we use 0, 1 , 2 ....
       # so we first need to create a adj list of size k 
       # and then we need to find the neighbours ( who is connected to whom)
       # this can be done by comparing letters in between 2 adjacent words in dict and see who comes
       # in front of whom ( that is who is connected to whom in our graph)
       # then when we have our grapsh we can return the order of words in the alien language

       # first step , built the graph

       adj = [[] for _ in range(K)]
       
       # find the neighbours in the graph
       for i in range(0, len(dict)-1):# till the last before word of the dict as we are comparing both words
          first_word = dict[i] # its a string 
          second_word = dict[i+1] # its a string
          j = 0
          while j<len(first_word) and j<len(second_word) and (first_word[j] == second_word[j]):
             j+=1
             pass
          # when we get to the charecter that is not equal 
          if j<len(first_word) and j<len(second_word):
            adj[ord(first_word[j])-ord('a')].append(ord(second_word[j])-ord('a')) # as our graph contains only numbers
        
        # now we have our graph us the topo sort
        # queue
       q = deque()
       # to store the order of words
       ans = []
       # indegree storage list
       indegree = [0]*K

       # popualted the indegree list
       for node in range(K):
          for neighbour in adj[node]:
             # store the indegree of the neigbour
             indegree[neighbour]+=1
        
        # now check for elements having zero indegree and add them to our list 
       for node in range(K):
          if indegree[node] == 0:
             # add to the queue
             q.append(node)
       while q:
          ele  = q.popleft()
          # add to our ans 
          ans.append(ele)

          # minius the indegree of ele"s neighbour by 1
          for neighbour in adj[ele]:
             indegree[neighbour]-=1
             # check if the indegre is zero
             if indegree[neighbour] == 0:
                # if yes them add it to the queue
                q.append(neighbour)

        # now just return the ans in string format
       return ''.join(chr(i+ord('a')) for i in ans)
                      
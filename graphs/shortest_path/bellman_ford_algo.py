class Solution:
    def bellman_ford(self, V, edges, S):
        # in this i try to code bellman ford algo 

        # in this algo we need to relax edges
        # this algo works for negative weighted graphs also unlike 
        # dijstras algo
        # it can also detect negative weighted cycles in our grph
        # note that a negative weighted cyclic graph has no shortest path solution
        # so its imp to indentify them
        # this algo mainly works on directed graphs 
        # but by 


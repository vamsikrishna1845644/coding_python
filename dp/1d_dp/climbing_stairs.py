class Solution:
    class Solution:
        def climbStairs(self, n: int) -> int:
            # this question is same as fibonnaci
            # not write the all code 
            # only writing the space optimizartion code
            prev2 = 1
            prev = 2
            if n == 0 or n == 1:
                return 1
            
            for _ in range(3,n+1):
                curr = prev2 + prev
                prev2 = prev
                prev = curr
            
            return prev
        
    
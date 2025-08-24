file:///c%3A/Users/ASUS/Desktop/coding_python/generate_parathesis.py {"mtime":1755438397977,"ctime":1755438397977,"size":0,"etag":"3em5h83ir0","orphaned":false,"typeId":""}
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # end the recursion when open == closed ==n
        # add open bracket when open < n
        # add clsoed bracket when closed < open
        stack = [] # temp variable
        result = [] # our finaly answer

        def backtrack(open , closed):

            if open == closed == n :
                result.append("".join(stack))
                return 
            
            if open < n:
                stack.append('(')
                backtrack(open + 1, closed)
                stack.pop()
            
            if closed < open :
                stack.append(')')
                backtrack(open , closed +1)
                stack.pop()
            # initiate backtraking
        backtrack(0,0)
        return result
    # we should pop the stack because , onece we add a charecter to the stack it then goves
    #deeper exploring that char and its next , after it explored it and stored the result in result variable
    # our stack is polluted with all expored chars , by poping we get our original stack to explore otehr 
    # possiblities
    
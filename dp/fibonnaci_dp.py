# in this we have to write the solution for fibonaacci using 
# recursion -> memoization ->tabulation -> space optimization
# recurion
n = int(input("enter value of n :"))
def fibonaaci(n):
    # base case

    if n == 0 or n == 1:
        return n
    
    return fibonaaci(n-1) + fibonaaci(n-2)

# this recurive solution works but as , its has a overlapping subproblem
# instaed of caluculating the ans to the subproblem each time 
# we can storee this ans 
# as this is a 1d dp ( meaning only one variable which is changing that is n)
# we can use a simple array of size n+1(we neesd to exclude zero ) to store
# our ans
# when we came back to same subproblem , insated of again calculating we can simply
# return the storeed values

# memoization(top to bottom)

dp = [-1 for _ in range(n+1) ] # initialise with -1

def fib(n,dp):
    # base case
    if n == 0 or n == 1:
        return n
    
    if dp[n] != -1:
        # meaning we already have the value of the sub problem with us 
        # no need to calculate again
        return dp[n]
    
    # if not
    # store the value and return 
    dp[n] = fib(n-1,dp) + fib(n-2,dp)
    return dp[n]


# tabulation ( bottom to up) # no recurion


def fib_tab(n,dp):
    dp[0] = 0
    dp[1] = 1
    if n == 0 or n == 1:
        return dp[n]
    
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]

# sapce optimization

# uses no extra space

def fib_so(n):
    if n == 0 or n == 1:
        return n
    prev2 = 0
    prev = 1
    for i in range(2,n+1):
        curri = prev2+prev
        prev2 = prev
        prev = curri
    
    return prev

print(fibonaaci(n))
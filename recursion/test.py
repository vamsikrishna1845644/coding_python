def solve_stack_optimization(threadSize):
    n=len(threadSize)
    if n<=2:return 0
    def cost(i):return max(0,max(threadSize[i-1],threadSize[i+1])+1-threadSize[i])
    dp=[(0,0) for _ in range(n)]
    dp[1]=(0,0)
    for i in range(2,n-1):
        not_special=dp[i-1]
        make_special=(dp[i-2][0]+1,dp[i-2][1]+cost(i))
        if make_special[0]>not_special[0]:dp[i]=make_special
        elif make_special[0]<not_special[0]:dp[i]=not_special
        else:dp[i]=(make_special[0],min(make_special[1],not_special[1]))
    return min(dp[n-2][1],dp[n-3][1]) if n>3 else dp[n-2][1]


threadSize = [3,1,4,5,5,2]
k = 2
print(solve_stack_optimization(threadSize))
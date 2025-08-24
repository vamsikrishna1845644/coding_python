def permutations(arr):
    # this is the main function
    ans = []
    map = {}
    temp = []
    recursive(arr, map ,ans ,temp)
    return ans
def recursive(arr, map ,ans ,temp):
    n = len(arr)
    # base case
    if len(temp) == len(arr):
        ans.append(temp[:])
        return
    # loop over
    for i in range(0,n):
        if i not in map:
            temp.append(arr[i])
            map[i] = 1
            recursive(arr,map,ans,temp)
            #pop then to explore other routes
            temp.pop()
            del map[i]

print(permutations([1, 2, 3]))

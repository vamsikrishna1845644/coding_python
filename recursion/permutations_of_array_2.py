def permutation(arr):
    # this is the main function
    ans  = []# main ans
    recursive(0 , arr ,ans)
    return ans
def recursive(index , arr , ans):
    n = len(arr)
    # base case
    if index == n:
        ans.append(arr[:])
    
    for i in range(index, n):
        arr[index] , arr[i] = arr [i] , arr[index] # swap the index with ith element
        recursive(index+1, arr , ans)
        arr[index] , arr[i] = arr [i] , arr[index] # unswap it , (backtracking) to explore other paths

arr = [5,9,3,4]
for p in permutation(arr):
    print(p)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # main function
        candidates =  sorted(candidates) # sort the array first
        ans = []
        temp = []
        self.recursive(0,target, candidates,ans,temp)
        return ans
    def recursive(self , ind , target , arr, ans ,temp ):
        # base case
        n = len(arr)
        if ( target == 0):
            ans.append(temp[:])
            return
        
        for i in range(ind ,n):
            # dont pick same element 
            if i > ind and arr[i] == arr[i-1]:
                continue
            # break if element is greater than target
            if arr[i] > target :
                break

            temp.append(arr[i])
            self.recursive(i+1, target - arr[i],arr ,ans ,temp)
            temp.pop()

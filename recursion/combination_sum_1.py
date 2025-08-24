class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # this is the return funtion  
        ans = []
        temp = []
        self.recursive(0, target , candidates, ans, temp)
        return ans
    def recursive(self, index , sum , arr , ans ,temp):
        # base case
        n = len(arr)
        if sum ==0 :
            ans.append(temp[:]) # copy of temp
            return
        if index >= n or sum < 0:
            return
        
        # pick
        temp.append(arr[index])
        self.recursive(index , sum - arr[index] , arr , ans ,temp)

        # not pick
        temp.pop()
        self.recursive(index+1 , sum , arr , ans ,temp)

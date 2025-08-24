class Solution:
    def subsetSums(self, nums):
        # this is the main function
        ans = []
        self.recursive(0, 0 , nums ,ans)
        ans = sorted(ans)
        return ans
    def recursive(self , index , sum , arr , ans ):
        n = len(arr)
        # base case
        if index >=n:
            ans.append(sum)
            return
        # pick
        self.recursive(index + 1 , sum + arr[index] , arr , ans)
        # not pick
        self.recursive(index + 1 , sum  , arr , ans)
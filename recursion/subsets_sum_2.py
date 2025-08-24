class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # main function
        # important point
        # all these are same model problems (combination sum and subsets sum)
        # forgot to sort
        nums = sorted(nums)
        ans = []
        temp = []
        self.recursive(0 , nums , ans , temp)
        return ans
    def recursive(self , index , arr , ans , temp):
        n = len(arr)
        # no base case as of
        # add elemets to the main list
        ans.append(temp[:])

        # loop overs
        for i in range(index, n):
            # dont take duplicates -> implemented before all these are same , put in mind
            if i!=index  and arr[i] == arr[i-1]:
                continue
            # pick the element
            temp.append(arr[i])
            self.recursive(i+1,arr,ans,temp)
            # pop
            temp.pop()


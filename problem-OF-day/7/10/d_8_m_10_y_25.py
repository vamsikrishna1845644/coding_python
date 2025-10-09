from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # doing this in a brute force manner
        # store ans
        ans = []
        # loop through each element in the spells
        for i in range(len(spells)):
            # to keep check of how many succesful pairs
            count = 0
            # for each element check how many successfully pairs it can form with portions
            for j in range(len(potions)):

                if spells[i]*potions[j] >= success:
                        count+=1
                    

            # store count in ans
            ans.append(count)  

        return ans


    def successfulPairs1(self, spells: List[int], potions: List[int], success: int) -> List[int]:
         # the optimal binary search way

         potions.sort() # sort the array

         # store the ans
         ans =[]

         # we need to find min_portion for each element and do a binary search of it in the sorted array

         for i in spells:
              min_portion = (success+i-1)//i # find the ciel of success/spell

              # using binary search find the min_portion or its slight greater elemts index in the sorted array
              index = bisect_left(potions,min_portion)

              count = len(potions) - index

              ans.append(count)
         return ans

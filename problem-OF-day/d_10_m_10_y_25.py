class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = 0
        empty = numBottles
        ans = numBottles
        while empty>=numExchange:
            full = empty//numExchange
            empty = empty%numExchange + full
            ans = ans+full
        return ans
sol = Solution()
print(sol.numWaterBottles(10,3))
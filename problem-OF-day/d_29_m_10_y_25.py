class Solution:
    def smallestNumber(self, n: int) -> int:
        # very easy diy

        return (1<<n.bit_length())-1
sol = Solution()
print(sol.smallestNumber(5))
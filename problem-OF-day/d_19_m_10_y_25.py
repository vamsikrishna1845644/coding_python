class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # very easy question
        # no comments needed

        # the second char of the tsring decides whats opertaion to perform to our variable

        # the ans variable initiated
        ans = 0
        for operation in operations:
            # the second charecter of the operations
            second_char = operation[1]

            if second_char == '+':
                ans+=1
            elif second_char == '-':
                ans-=1
            
        return ans

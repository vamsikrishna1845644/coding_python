class Solution:
    def reverseStack(self, stack):
        if not stack:
            return stack
        top = stack.pop()

        self.reverseStack(stack)

        self. insertatbottom(stack,top)
        return stack

    def insertatbottom(self,stack,element):
        if not stack :
            stack.append(element)
            return
        
        top = stack.pop()
        self.insertatbottom(stack,element)

        stack.append(top)
        



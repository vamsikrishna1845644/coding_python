class Solution:
    def sortStack(self, stack):
        element = stack.pop()
        self.sortStack(stack)

        self.insertsorted(stack, element)
        return stack
    
    def insertsorted(self, stack , element):
        if not stack or element >= stack[-1]:
            stack.append(element)
            return
        
        top = stack.pop()
        self.insertsorted(stack,top)

        stack.append(top)
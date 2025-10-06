from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # trail to test my new keyboard
        # doing in normal method
        if head is not None:
            right = head.next # pointer to the right of head
        else:
            return None
        left = None # this is the left most pointer
        temp = head
        while temp is not None:
            temp.next = left
            left = temp
            temp = right
            if right is not None:
                right = right.next
            else:
                right = None
        return left
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find the lenght of the ll
        temp = head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        
        middle = count//2 + 1
        temp = head

        while middle!=1 and temp:
            middle-=1
            temp = temp.next
            
        
        return temp
    class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # we know this from the merge sort video
            temp = ListNode(0)
            head = temp
            temp1 = list1
            temp2 = list2

            while temp1 is not None and temp2 is not None:
                if ( temp1 is not None and temp2 is not None) and temp1.val>=temp2.val:
                    temp.next = temp2
                    temp = temp.next
                    temp2 = temp2.next
                if ( temp1 is not None and temp2 is not None) and temp1.val<temp2.val:
                    temp.next = temp1
                    temp = temp.next
                    temp1 = temp1.next
            # we still have to nadd the remaining elemnets
            while temp1 is None and temp2 is not None:
                # add the remainig temp2 elements
                temp.next = temp2
                temp = temp.next
                temp2 = temp2.next
            while temp1 is not None and temp2 is None:
                # add the remainig temp2 elements
                temp.next = temp1
                temp = temp.next
                temp1 = temp1.next
            return head.next






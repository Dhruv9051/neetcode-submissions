# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a placeholder node to start the new list
        dummy = ListNode()
        curr = dummy

        # 2. Use the variable names provided in the function arguments (list1, list2)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next  # Move list1 pointer forward
            else:
                curr.next = list2
                list2 = list2.next  # Move list2 pointer forward
            
            curr = curr.next        # Move the 'tail' of our new list forward

        # 3. If one list is longer than the other, attach the remainder
        # We use a simple 'or' here because if list1 is null, it attaches list2 (and vice versa)
        curr.next = list1 or list2

        # 4. Return dummy.next (the actual first node of our merged list)
        return dummy.next
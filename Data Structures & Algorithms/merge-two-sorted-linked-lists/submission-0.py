# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode(0)
   
        current = dummy
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        while list1 or list2:
            if list1 is None:
                current.next=list2
                return dummy.next
            elif list2 is None:
                current.next=list1
                return dummy.next

            if list1.val <= list2.val:
                print(f"list1.val: {list1.val}")
                current.next = list1
                current = current.next
                print(f"current.val: {current.val}")
                list1 = list1.next
            else:
                print(f"list2.val: {list2.val}")
                current.next = list2
                current = current.next
                print(f"current.val: {current.val}")
                list2 = list2.next

        return dummy.next

            
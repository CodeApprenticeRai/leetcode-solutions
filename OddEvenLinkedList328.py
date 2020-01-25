# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if ((type(head) == type(None)) or (type(head.next) == type(None))):
            return head

        odd_head = head
        even_head = head.next

        odd_curr = odd_head
        even_curr = even_head

        while (True):
            if (type(even_curr.next) != type(None)):
                odd_curr.next = even_curr.next
                odd_curr = odd_curr.next
            else:
                odd_curr.next = even_head
                return head

            if (type(odd_curr.next) != type(None)):
                even_curr.next = odd_curr.next
                even_curr = even_curr.next
            else:
                even_curr.next = None
                odd_curr.next = even_head
                return head
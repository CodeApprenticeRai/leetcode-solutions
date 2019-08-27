from .ListNode import ListNode

class LinkedListHelper:
    '''
    Given an array of integers,
    return the head of a Linked List representation of the array of integers
    '''
    def to_linked_list(self, arr):
        head = None
        _prev = None
        for i in range(len(arr)):
            if not head:
                head = ListNode(arr[i])
                _prev = head
            else:
                _prev.next = ListNode(arr[i])
                _prev = _prev.next
        return head
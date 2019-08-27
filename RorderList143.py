# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
    Solution:
    'Arrayize' the list ( store the list in an array)
'''

from algorithm_helpers.LinkedListHelper import LinkedListHelper

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        array = []
        curr = head
        while (curr != None):
            array.append(curr)
            curr = curr.next

        i = 0
        j = len(array) - 1
        toggle = True

        while (i < j):
            if (toggle):
                array[i].next = array[j]
                i += 1
            else:
                array[j].next = array[i]
                j -= 1
            toggle = not toggle

        array[i].next = None

        return head

linked_list_helper = LinkedListHelper()
sol = Solution()
test_data = [
    [1,2,3,4],
    # [1,2,3,4,5]
]
test_data = [ linked_list_helper.to_linked_list(test_data[i]) for i in range(len(test_data) ) ]

for i in range(len(test_data)):
    sol.reorderList(test_data[i])
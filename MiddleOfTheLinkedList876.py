# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
1-> 0
2-> 1
3-> 1
4-> 2


Keep:
    pointer to the middle item of the list,
    pointer to the last read value of the list,
    length of the values we've read

Increment the middle pointer

'''


class Solution:
    def middleNode(self, head):
        arr = []

        curr = head

        while (curr != None):
            arr.append(curr)
            curr = curr.next

        return arr[len(arr) // 2]

    # o(1) runtime, o(1) space
#     def middleNode(self, head):
#         curr = head
#         middle = head
#         stream_length= 1

#         while (curr != None):
#             curr= curr.next

#             if ( curr != None ):
#                 stream_length += 1

#             # increment our middle pointer, each time the stream_length is even
#             if ( (stream_length-1) % 2 == 0 ):
#                 middle = middle.next


#         return middle

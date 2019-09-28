# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# from collections import deque

'''
    Here the idea is to just make sure that we can always retrieve the smallest element


    * push all the list heads into a min heap based on value
    * while the heap is not empty
        *
        on the first go around set the list head
        if type(curr.next) != type(None):
            set curr.next
        set curr = minheap.pop()
        if type(curr.next) != type(None):
            push minheap.push(curr.next)


'''

import heapq


class Solution:
    def mergeKLists(self, lists):
        curr = None
        head = None
        min_heap = []

        for list_head in lists:
            if (type(list_head) != type(None)):
                heapq.heappush(min_heap, (int(list_head.val), id(list_head), list_head))

        while (len(min_heap) > 0):
            if (head == None):
                head = heapq.heappop(min_heap)[2]
                if (type(head.next) != type(None)):
                    heapq.heappush(min_heap, (int(head.next.val), id(head.next), head.next))
                curr = head
            else:
                curr.next = heapq.heappop(min_heap)[2]
                curr = curr.next
                if (type(curr.next) != type(None)):
                    heapq.heappush(min_heap, (int(curr.next.val), id(curr.next), curr.next))

        return head


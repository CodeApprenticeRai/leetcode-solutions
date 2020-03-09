class DLLNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.direct_access_map = {}
        self.MRU = None
        self.LRU = None

    def get(self, key: int) -> int:
        if key in self.direct_access_map:
            accessed_node = self.direct_access_map[key]
            self.promote_to_MRU(accessed_node, False)
            return accessed_node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.direct_access_map:
            accessed_node = self.direct_access_map[key]
            accessed_node.value = value

            self.promote_to_MRU(accessed_node, False)

        else:
            accessed_node = DLLNode(key, value)
            self.direct_access_map[key] = accessed_node
            self.promote_to_MRU(accessed_node, is_newly_created_node=True)
        return None

    def promote_to_MRU(self, accessed_node, is_newly_created_node):
        # Case list was empty:
        if (self.current_capacity == 0):
            self.LRU = accessed_node
            self.MRU = accessed_node
            self.current_capacity += 1

        # Case we accessed the MRU : do nothing
        elif (id(accessed_node) == id(self.MRU)):
            pass

        # Case we just created a node: add it to the front of the list and update MRU and capacity
        elif (is_newly_created_node):
            accessed_node.next = None
            accessed_node.prev = self.MRU
            self.MRU.next = accessed_node
            self.MRU = accessed_node
            self.current_capacity += 1

        # Case the node exist in the list but is not the first or last element
        elif ((id(accessed_node) != id(self.MRU) and (id(accessed_node) != id(self.LRU)))):  # if
            accessed_node.prev.next = accessed_node.next
            accessed_node.next.prev = accessed_node.prev

            accessed_node.next = None
            accessed_node.prev = self.MRU
            self.MRU.next = accessed_node
            self.MRU = accessed_node

        # Case the node is only the last element and not the first
        elif (id(accessed_node) == id(self.LRU)):
            self.LRU = self.LRU.next
            self.LRU.prev = None
            self.MRU.next = accessed_node
            accessed_node.prev = self.MRU
            accessed_node.next = None
            self.MRU = accessed_node

        # update LRU by eviction if we go over max_capacity
        if (self.current_capacity > self.max_capacity):
            temp_LRU_pointer = self.LRU
            self.LRU = self.LRU.next
            temp_LRU_pointer.next = None
            self.LRU.prev = None
            del self.direct_access_map[temp_LRU_pointer.key]
            del temp_LRU_pointer
            self.current_capacity -= 1
        return None


cache = LRUCache(3)
cache.put(1, 1) #MRU=LRU=1
cache.put(2, 2) # 1-2
cache.put(3, 3) # 1-2-3
cache.put(4, 4) # 2-3-4
cache.get(4) # 2-3-4
cache.get(3) # 2-4-3
cache.get(2) # 4-3-2
cache.get(1) # return -1
cache.put(5,5) #3-2-5
cache.get(1)
cache.get(2)
cache.get(3)
cache.get(4)
cache.get(5)


# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1)     #// returns 1
# cache.put(3, 3)    #// evicts key 2
# cache.get(2)     #// returns -1 (not found)
# cache.put(4, 4)    #// evicts key 1
# cache.get(1)       #// returns -1 (not found)
# cache.get(3)       #// returns 3
# cache.get(4)       #// returns 4


# cache = LRUCache(1)
# cache.put(1,1)
# cache.put(1,2)
# cache.put(2,2)
# cache.put(2,3)
# cache.get(1)
# cache.get(2)
# # cache.put(2, 1)
# cache.put(2, 2)
# cache.get(2)
# cache.put(3, 2)
# cache.get(2)
# cache.put(4, 4)
# cache.get(1)
# cache.get(3)
# cache.get(4)
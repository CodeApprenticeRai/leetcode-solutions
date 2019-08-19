'''
    A heap is a way to construct a sorted collection of items with
    O( log(n) ) insert, and O( log(n) ) retrieval of the max/min element:

    I found it useful for the problem of Merging K Sorted Lists
'''
import math

#I'll implement a min-heap first and then if I still have energy I'll try to make the min/max setting a parameter configuration
class Heap:
    def __init__(self, compare_function=lambda x: x):
        self.heap = []
        self.compare_function = compare_function

    def get_top(self):
        if self.heap:
            return self.heap[-1]

    def pop(self):
        if not self.heap:
            return None
        elif (len(self.heap) == 1):
            return self.heap.pop()
        else:
            i = 0
            top = self.heap.pop()
            self.heap[i] = top

            #compare value at self.heap[i] with children if they exist, swap with the child that has the smallest value, i becomes the
            while(True):
                index_of_left_child = self.get_left_child_index(i)
                index_of_right_child = self.get_right_child_index(i)
                index_of_child_with_lesser_value = None

                if (index_of_left_child < len(self.heap)):
                    index_of_child_with_lesser_value = index_of_left_child
                if (index_of_right_child < len(self.heap)):
                    #: index_of_child_with_lesser_value = min( index_of_left_child, index_of_right_child)
                    index_of_child_with_lesser_value = index_of_left_child if ( self.compare_function(self.heap[index_of_left_child]) < self.compare_function(self.heap[index_of_right_child])) else index_of_right_child
                if ( ( type(index_of_child_with_lesser_value) == type(None)) or (self.compare_function(self.heap[i]) < self.compare_function(self.heap[index_of_child_with_lesser_value]))):
                    return top
                # else: swap
                temp = self.heap[index_of_child_with_lesser_value]
                self.heap[index_of_child_with_lesser_value] = self.heap[i]
                self.heap[i] = temp
                i = index_of_child_with_lesser_value

    def insert(self, item): # item can be any type: by unenforced convention all items in self.heap should be of the same type
        self.heap.append(item)
        i = len(self.heap) -1

        i_parent = self.get_parent_index(i)
        while( (i > 0) and  (self.compare_function(self.heap[i_parent]) > self.compare_function(self.heap[i]) ) ):
            #swap the two items
            temp = self.heap[i_parent]
            self.heap[i_parent] = self.heap[i]
            self.heap[i] = temp
            i = i_parent
            i_parent = self.get_parent_index(i)
        
        return None
    
    def get_parent_index(self, i):
        return math.floor(i/2)
    
    def get_left_child_index(self, i):
        return (2 * i) + 1
    
    def get_right_child_index(self, i):
        return (2 * i) + 2

    def __len__(self):
        return len(self.heap)


#tests
if __name__ == '__main__':
    heap = Heap()

    #test 1
    # for i in range(10, 21):
    #     heap.insert(i)

    #test 2
    # heap.insert(10)
    # heap.insert(9)
    # heap.insert(11)
    # heap.insert(8)
    # heap.insert(4)
    # heap.insert(7)
    # heap.pop()
    # heap.pop()
    # heap.pop()
    # heap.pop()
    # heap.pop()
    # heap.pop()
    # heap.pop()
    # heap.pop()
    # print(heap.heap)

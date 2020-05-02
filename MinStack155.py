'''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.


'''



class DLLNode:
    def __init__(self, value, _prev=None, _next=None):
        self.value = value
        self.prev = _prev
        self.next = _next


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0
        self.min_history_stack = []
        self.top_node = None
        self.bottom_node = None

    def push(self, x: int) -> None:
        new_node = DLLNode(x)

        # update min
        if ((len(self.min_history_stack) == 0) or (x < self.min_history_stack[-1].value)):
            self.min_history_stack.append(new_node)

        # link new_node and previous top, else update bottom
        if (self.size > 0):
            self.top_node.next = new_node
            new_node.prev = self.top_node
        else:
            self.bottom_node = new_node

        self.top_node = new_node
        self.size += 1

        return None

    def pop(self) -> None:
        if (self.size > 0):
            # update min
            if (id(self.min_history_stack[-1]) == id(self.top_node)):
                self.min_history_stack.pop()
            new_top = self.top_node.prev

            # update top, and bottom if necessary
            if (new_top != None):
                new_top.next = None
            else:
                self.bottom_node = None

            del self.top_node
            self.top_node = new_top
            self.size -= 1
        return None

    def top(self) -> int:
        return self.top_node.value

    def getMin(self) -> int:
        if (len(self.min_history_stack) == 0):
            raise Exception("The list has no elements")
        return self.min_history_stack[-1].value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
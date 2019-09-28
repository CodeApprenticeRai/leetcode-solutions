'''
    There are a total of n courses you have to take,
    labeled from 0 to n-1

    Some courses may have prerequisites, 1 -> 0 : [ 0, 1]

    You are give a list of 2-tuples [ course, pre_req ]

    Return the ordering of courses you should take to finish all courses.

'''

'''
    Algorithm:

    Sort nodes by increasing in-degree:
        Step:
            Visit the node with the lowest indegree: ( for the first go around this will be a node where the indegree is 0):
                Delete the outgoing edges from that node in order to update the in-degree of all nodes directly conencted to it
                Add node.value to our topologically sorted list


'''
from collections import deque


class Solution:
    def createEdge(self, from_value, to_value):
        if from_value not in self.nodes:
            self.nodes[from_value] = {
                "incoming": {},
                "outgoing": {}
            }
        if to_value not in self.nodes:
            self.nodes[to_value] = {
                "incoming": {},
                "outgoing": {}
            }

        self.nodes[from_value]["outgoing"][to_value] = True
        self.nodes[to_value]["incoming"][from_value] = True
        return None

    def removeEdge(self, from_value, to_value):
        del self.nodes[from_value]["outgoing"][to_value]
        del self.nodes[to_value]["incoming"][from_value]
        return None

    def getIndegree(self, value):
        if value in self.nodes:
            return len(self.nodes[value]["incoming"])
        else:
            return None

    # def cycleDetected(self, from_value, to_value):
    # return (from_value in self.nodes[to_value]["incoming"] ) and ( to_value in self.nodes[from_value]["incoming"] )

    def pathExists(self, curr_value, goal_value):
        if (curr_value == goal_value):
            return True

        path_exists = False
        for node_value in self.nodes[curr_value]["outgoing"]:
            path_exists = path_exists or self.pathExists(node_value, goal_value)
            if path_exists:
                break

        return path_exists

    def findOrder(self, numCourses, prerequisites):
        self.nodes = {
            i: {
                "incoming": {},
                "outgoing": {}
            }
            for i in range(numCourses)
        }

        # Create graph as an adjacency map where each node holds the information about all it's incoming and outgoing nodes
        for edge in prerequisites:
            if self.pathExists(edge[0], edge[
                1]):  # given edge [ to_node, from_node ], if a path from to_node to from_node exists, we'll be creating a cycle by creating edge: from_node --> to_node, a cycle will make our solution the empty set
                return []
            self.createEdge(edge[1], edge[0])

        # Initialize a queue to contain also the nodes that have in-degree == 0
        queue = deque()

        for node_value in self.nodes:
            if (self.getIndegree(node_value) == 0):
                queue.append(node_value)

        topological_sorting = []
        # While this queue is not empty:
        while (len(queue) > 0):
            curr = queue.popleft()

            edges_to_remove = []
            for node_value in self.nodes[curr]["outgoing"]:
                if ((self.getIndegree(node_value) - 1) == 0):
                    queue.append(node_value)
                edges_to_remove.append(node_value)

            for node_value in edges_to_remove:
                self.removeEdge(curr, node_value)

            topological_sorting.append(curr)

        return topological_sorting


sol = Solution()
sol.findOrder(3, [[1,0],[1,2],[0,1]])

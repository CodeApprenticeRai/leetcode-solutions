'''
    Given the edges of a directed graph
    and two nodes source and destination of this graph:

    determine whether or not all paths starting at source
    eventually end at destination:

    -At least one path exists from the source node to the destination node
    -If a path exists from the source node to a node with no outgoing edges,
        then that node is equal to destination.
    -The number of possible paths from source to destination is a finite number.

'''

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

    def only_goes_to_destination( self, node_key, search_path):
        if node_key in self.solution_memo__only_goes_to_destination:
            return self.solution_memo__only_goes_to_destination[node_key]

        elif node_key in search_path:
            self.solution_memo__only_goes_to_destination[node_key] = False
            return self.solution_memo__only_goes_to_destination[node_key]

        else:
            search_path[node_key] = True
            if ( len( self.nodes[node_key]["outgoing"] ) == 0 ):
                # this node is not destination, therefore it is a terminal node that isn't destination
                self.solution_memo__only_goes_to_destination[node_key] = False
            else:
                _solution = True
                for outgoing_node_key in self.nodes[node_key]["outgoing"]:
                    _solution = _solution and self.only_goes_to_destination(outgoing_node_key, search_path)
                    if (not _solution):
                        break
                self.solution_memo__only_goes_to_destination[node_key] = _solution

            return self.solution_memo__only_goes_to_destination[node_key]

    def leadsToDestination(self, n, edges, source, destination):
        # create all nodes
        self.nodes = {
            i: {
                "incoming": {},
                "outgoing": {}
            }
            for i in range(n)
        }

        # create all edges
        for edge in edges:
            self.createEdge(edge[0], edge[1])

        if  ( len(self.nodes[destination]["outgoing"]) > 0 ):
            return False
        else:
            self.solution_memo__only_goes_to_destination = { destination: True }



        if (len( self.nodes[source]["outgoing"] ) > 0):
            for outgoing_node_key in self.nodes[source]["outgoing"]:
                if ( not self.only_goes_to_destination( outgoing_node_key, {} ) ):
                    return False
        else:
            if (source == destination):
                return True
            else:
                return False

        return True
sol = Solution()
print( sol.leadsToDestination(5, [[0,1],[1,2],[2,3],[3,4]], 1, 3) == False )
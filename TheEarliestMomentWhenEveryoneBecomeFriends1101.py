class PersonNode:
    def __init__(self, key):
        self.key = key
        self.friends = {}


class FriendsGraph:
    def __init__(self):
        self.persons = {}
        pass

    def __contains__(self, key_of_person):
        return key_of_person in self.persons

    def put(self, key):
        if key not in self.persons:
            self.persons[key] = PersonNode(key)
        else:
            raise KeyError("Key '{}' already exists -- no duplicate keys allowed".format(key))
        return None

    def acquaint(self, key1, key2):
        if ((key1 in self.persons) and (key2 in self.persons)):
            person1 = self.persons[key1]
            person2 = self.persons[key2]

            person1.friends[key2] = person2
            person2.friends[key1] = person1

        else:
            raise KeyError("Cannot acquaint '{}' and '{}' -- one of these person do not exist in graph".format(key))
        return None

    '''
        A graph is N-fully connected if there are N-nodes in the graph, and all nodes can be reached from all other nodes
        This function returns whether that condition is true for the graph object it is called from
    '''

    def is_n_fully_connected(self, N):
        if (len(self.persons) == 0):
            return False
        else:
            random_person_key, random_person_node = self.persons.popitem()
            self.persons[random_person_key] = random_person_node

            self.nodes_found_in_dfs_starting_at_a_random_node = {}  # !!! bad variable name
            self.update_nodes_found_in_dfs_starting_at_a_random_node(random_person_node)  # !!! bad variable name

            return len(self.nodes_found_in_dfs_starting_at_a_random_node) == N

    def update_nodes_found_in_dfs_starting_at_a_random_node(self, current_node):  # !!! bad variable name
        if current_node.key in self.nodes_found_in_dfs_starting_at_a_random_node:  # !!! bad variable name
            return len(self.nodes_found_in_dfs_starting_at_a_random_node)  # !!! bad variable name
        else:
            self.nodes_found_in_dfs_starting_at_a_random_node[current_node.key] = current_node  # !!! bad variable name
            for person_key in current_node.friends:
                self.update_nodes_found_in_dfs_starting_at_a_random_node(
                    current_node.friends[person_key])  # !!! bad variable name
            return len(self.nodes_found_in_dfs_starting_at_a_random_node)


class Solution:
    def earliestAcq(self, logs, N):
        logs.sort(key=lambda log_list: log_list[0])
        friends_graph = FriendsGraph()
        i = 0

        while ((i < len(logs))):
            if logs[i][1] not in friends_graph:
                friends_graph.put(logs[i][1])
            if logs[i][2] not in friends_graph:
                friends_graph.put(logs[i][2])

            friends_graph.acquaint(logs[i][1], logs[i][2])

            if friends_graph.is_n_fully_connected(N):
                return logs[i][0]
            i += 1
        return -1

sol = Solution()
# print( sol.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6) )
print( sol.earliestAcq([[3,0,3],[4,1,2],[0,2,0],[2,0,2],[8,0,3],[1,0,1],[5,1,2],[7,3,1],[6,1,0],[9,3,0]], 4))
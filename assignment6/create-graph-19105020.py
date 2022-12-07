class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Graph:
    # Constructor initializes an empty dictionary
    def __init__(self):
        self.al = {}


    """ This method adds a node to the graph in the form of an (key, value) pair. The key being the node itself
        and the value is the list of nodes that can be accessed from that node. This is called an adjacency list.
    """

    def addNode(self, node, lst):
        self.al[node] = lst

    """ Code for traversing the graph in Breadth First Search manner. This is level-wise searching.
        This gives us shortest path from one node to another. """

    def bfs(self, node):
        print (node.name)
        level = {node: 0}
        """
        level is a dictionary which holds all the visited nodes and their levels.
        This dictionary is looked up every time we want to see if a node has been visited.
        """

        parent = {node: None}

        i = 1  # i is for keeping track of the levels

        frontier = [node]
        """
        This will be assigned as a new list in every iteration.
        This will have the list of nodes adjacent to the current node till no node is left un-visited.
        """

        while frontier:
            next_node = []
            """
            next_node is a temporary list to hold the values that would become the next frontiers
            """

            for u in frontier:
                for v in self.al[u]:
                    if v not in level:
                        print (v.name)
                        level[v] = i
                        parent[v] = u
                        next_node.append(v)

            frontier = next_node
            i += 1
        return level

    def dfs_visit(self, x, visited):
        if x in visited.keys():
            return
        else:
            print (x.name)
            visited[x] = True
            for w in self.al[x]:
                self.dfs_visit(w, visited)

    def depth_first(self, node):
        print (node.name)
        visited = {node: True}

        for w in self.al[node]:
            self.dfs_visit(w, visited)


def main():
    a = Node('a', 5)
    b = Node('b', 3)
    c = Node('c', 6)
    d = Node('d', 7)
    e = Node('e', 9)

    g = Graph()
    g.addNode(a, [b, d])
    g.addNode(b, [a, c, d])
    g.addNode(c, [b, d, e])
    g.addNode(d, [a, b, c, e])
    g.addNode(e, [d, c])

    print("BFS :")
    g.bfs(a)
    print("DFS :")
    g.depth_first(a)


if __name__ == '__main__':
    main()
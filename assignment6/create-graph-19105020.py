from collections import defaultdict
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

def dfs(visited, graph, node): 
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

visited2 = set() # List for visited nodes
queue = []       # Initialize a queue

def bfs(visited2, graph, node): # function for BFS
  visited2.add(node)
  queue.append(node)
  while queue:                  # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 
    for neighbour in graph[m]:
      if neighbour not in visited2:
        visited2.add(neighbour)
        queue.append(neighbour)

addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','f')
addEdge(graph,'c','g')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

visited = set() # Set to keep track of visited nodes of graph.
print("Following is the Depth-First Search")
dfs(visited, graph, 'a')
print("\nFollowing is the Breadth-First Search")
bfs(visited2, graph, 'a')
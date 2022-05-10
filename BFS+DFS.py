# Week 4
from queue import Queue
graph = {
    'a' : ['b', 'c'],
    'b' : ['a', 'd', 'e'],
    'c' : ['a', 'f'],
    'd' : ['b','e'],
    'e' : ['g','d','b'],
    'f' : ['c','g'],
    'g' : [ 'e','f'] 
}
visited = set() 
def dfs(visited, graph, node): 
    if node not in visited:
        print (node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
def traversal(adj_list, start_node):
    visited = set()
    queue = Queue()
    queue.put(start_node)
    visited.add(start_node)
    while not queue.empty():
        current_node = queue.get()
        print(current_node, end = " ")
        for next_node in adj_list[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                visited.add(next_node)
if __name__ == '__main__':
  print("Depth-First Search Traversal")
  dfs(visited, graph, 'a')
  print("\nBreadth first Search Traversal")
  traversal(graph, 'a')
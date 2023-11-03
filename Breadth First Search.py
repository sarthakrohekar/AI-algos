graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}


#bfs algo implementation
def bfs(start):
    queue = [start]
    levels ={}
    levels[start] = 0
    visited = set([start])
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                levels[neighbour] = levels[node] + 1
    print("levels of all nodes:")
    print(levels)
    print("visited nodes:")
    return visited
print(str(bfs('C')))

#for finding bfs path from start to goal
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
result = list(bfs_paths(graph,'C','A'))
print("All the possible paths:")
print(result)

#finding the shortest path from all possible paths
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


resultshortest = shortest_path(graph, 'C', 'A')
print("The shortest path is:")
print(resultshortest)
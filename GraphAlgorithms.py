class ShortestPathResult:
    def __init__(self, is_success, path_array):
        self.is_success = is_success
        self.path_array = path_array

def bfs_shortest_path(graph, source, destination):
    visited = []
    queue = [[source]]
 
    if source == destination:
        return ShortestPathResult(True, list([source]))

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == destination:
                    return ShortestPathResult(True, new_path)
            visited.append(node)

    return ShortestPathResult(False, None)
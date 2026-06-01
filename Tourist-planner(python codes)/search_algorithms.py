from collections import deque
import heapq

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                new_path = path + [neighbour]
                queue.append(new_path)

    return None


def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                new_path = path + [neighbour]
                stack.append(new_path)

    return None


def ucs(graph, start, goal):
    priority_queue = [(0, [start])]

    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        node = path[-1]

        if node == goal:
            return path, cost

        for neighbour, distance in graph[node].items():
            if neighbour not in path:
                new_path = path + [neighbour]
                new_cost = cost + distance
                heapq.heappush(priority_queue, (new_cost, new_path))

    return None, float("inf")


def a_star(graph, start, goal, heuristic):
    priority_queue = [(0, 0, [start])]

    while priority_queue:
        estimated_cost, actual_cost, path = heapq.heappop(priority_queue)
        node = path[-1]

        if node == goal:
            return path, actual_cost

        for neighbour, distance in graph[node].items():
            if neighbour not in path:
                new_actual_cost = actual_cost + distance
                new_estimated_cost = new_actual_cost + heuristic.get(neighbour, 0)
                new_path = path + [neighbour]
                heapq.heappush(priority_queue, (new_estimated_cost, new_actual_cost, new_path))

    return None, float("inf")
print("search_algorithms loaded")
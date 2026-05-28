# ==========================================
# TOURIST ROUTE PLANNER USING AI CONCEPTS
# ==========================================

from collections import deque
import heapq

# ------------------------------------------
# GRAPH REPRESENTATION
# ------------------------------------------

graph = {
    'Beach': {'Museum': 4, 'Park': 2},
    'Museum': {'Temple': 5, 'Mall': 10},
    'Park': {'Mall': 3, 'Temple': 7},
    'Temple': {'Zoo': 6},
    'Mall': {'Zoo': 1},
    'Zoo': {}
}

# ------------------------------------------
# BFS ALGORITHM
# ------------------------------------------

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

# ------------------------------------------
# DFS ALGORITHM
# ------------------------------------------

def dfs(start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(neighbor, goal, path)

            if new_path:
                return new_path

    return None

# ------------------------------------------
# UNIFORM COST SEARCH (UCS)
# ------------------------------------------

def ucs(start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node].items():
                heapq.heappush(
                    priority_queue,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return float("inf"), []

# ------------------------------------------
# CONSTRAINT SATISFACTION
# ------------------------------------------

def filter_places(budget, preferred_places):
    place_cost = {
        'Beach': 2,
        'Museum': 5,
        'Park': 3,
        'Temple': 4,
        'Mall': 6,
        'Zoo': 5
    }

    result = []

    for place in preferred_places:
        if place_cost[place] <= budget:
            result.append(place)

    return result

# ------------------------------------------
# MINIMAX ALGORITHM
# ------------------------------------------

def minimax(depth, node_index, maximizing_player,
            values, alpha, beta):

    if depth == 3:
        return values[node_index]

    if maximizing_player:
        best = -1000

        for i in range(2):
            value = minimax(
                depth + 1,
                node_index * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        for i in range(2):
            value = minimax(
                depth + 1,
                node_index * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

# ------------------------------------------
# BAYESIAN STYLE UNCERTAINTY
# ------------------------------------------

def weather_prediction(weather):
    probability = {
        'Sunny': 0.8,
        'Rainy': 0.3,
        'Cloudy': 0.6
    }

    return probability.get(weather, 0.5)

# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

print("\n========= TOURIST ROUTE PLANNER =========\n")

start = 'Beach'
goal = 'Zoo'

# BFS
print("1. BFS Path:")
print(bfs(start, goal))

# DFS
print("\n2. DFS Path:")
print(dfs(start, goal))

# UCS
print("\n3. Uniform Cost Search:")
cost, path = ucs(start, goal)
print("Optimal Path:", path)
print("Minimum Cost:", cost)

# Constraint Satisfaction
print("\n4. Constraint Satisfaction:")

budget = 4
preferred = ['Beach', 'Museum', 'Park', 'Temple']

filtered = filter_places(budget, preferred)

print("Budget:", budget)
print("Places within budget:", filtered)

# Minimax
print("\n5. Minimax Decision Making:")

values = [3, 5, 2, 9, 12, 5, 23, 23]

optimal_value = minimax(
    0,
    0,
    True,
    values,
    -1000,
    1000
)

print("Optimal Decision Value:", optimal_value)

# Bayesian Reasoning
print("\n6. Weather Probability Prediction:")

weather = "Sunny"

prob = weather_prediction(weather)

print(f"Weather: {weather}")
print(f"Travel Suitability Probability: {prob}")

print("\n========= SYSTEM OUTPUT =========")
print("Recommended Route:", path)
print("Reason:")
print("- Minimum distance")
print("- Budget friendly")
print("- Preferred tourist locations")
print("- Weather suitable")
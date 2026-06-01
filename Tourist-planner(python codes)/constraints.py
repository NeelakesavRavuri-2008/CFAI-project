def calculate_route_details(route, graph):
    total_distance = 0

    for i in range(len(route) - 1):
        source = route[i]
        destination = route[i + 1]
        total_distance += graph[source][destination]

    cost = total_distance * 10
    time = total_distance * 5

    return total_distance, cost, time


def check_constraints(route, graph, budget, max_time):
    distance, cost, time = calculate_route_details(route, graph)

    if cost <= budget and time <= max_time:
        return True, distance, cost, time

    return False, distance, cost, time
from locations import graph, place_type
from search_algorithms import bfs, dfs, ucs, a_star
from constraints import check_constraints
from recommendation import calculate_preference_score, final_score
from uncertainty import adjust_for_traffic_and_weather
from explanation import explain_output


heuristic = {
    "Charminar": 12,
    "Salar Jung Museum": 8,
    "Birla Mandir": 10,
    "Hussain Sagar": 5,
    "Golconda Fort": 0
}


def main():
    print("Available Places:")
    for place in graph:
        print("-", place)

    start = input("\nEnter start location: ")
    goal = input("Enter destination: ")
    budget = int(input("Enter budget: "))
    max_time = int(input("Enter available time in minutes: "))
    preference = input("Enter preference Historical/Museum/Temple/Nature: ")
    traffic = input("Enter traffic condition light/medium/heavy: ")
    weather = input("Enter weather condition clear/cloudy/rainy: ")

    if start not in graph or goal not in graph:
        print("Invalid start or destination.")
        return

    route, distance = a_star(graph, start, goal, heuristic)

    if route is None:
        print("No route found.")
        return

    valid, distance, cost, time = check_constraints(route, graph, budget, max_time)

    adjusted_time, extra_time = adjust_for_traffic_and_weather(time, traffic, weather)

    if adjusted_time > max_time:
        print("\nNo valid route found within the given time after traffic/weather adjustment.")
        print("Route found:", " -> ".join(route))
        print("Normal Time:", time, "minutes")
        print("Extra Time:", extra_time, "minutes")
        print("Final Time:", adjusted_time, "minutes")
        return

    if valid:
        preference_score = calculate_preference_score(route, place_type, preference)
        score = final_score(distance, cost, adjusted_time, preference_score)

        explain_output(route, distance, cost, adjusted_time, score, preference)
    else:
        print("\nNo valid route found within budget or time.")


main()
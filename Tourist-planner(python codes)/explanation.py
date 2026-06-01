def explain_output(route, distance, cost, time, score, preference):
    print("\n========== TOURIST ROUTE PLANNER ==========")

    print("\nRecommended Route:")
    print(" -> ".join(route))

    print("\nRoute Details:")
    print("Total Distance:", distance, "km")
    print("Estimated Cost: Rs.", cost)
    print("Estimated Time:", time, "minutes")
    print("Final Route Score:", score)

    print("\nReason:")
    print("- Route satisfies budget constraints")
    print("- Route satisfies time constraints")
    print("- Route matches user preference:", preference)
    print("- Traffic and weather are considered")

    print("\n==========================================")
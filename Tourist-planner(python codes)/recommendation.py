def calculate_preference_score(route, place_type, preference):
    score = 0

    for place in route:
        if place_type[place] == preference:
            score += 10
        else:
            score += 2

    return score


def final_score(distance, cost, time, preference_score):
    score = 100

    score -= distance * 2
    score -= cost * 0.02
    score -= time * 0.1
    score += preference_score

    return round(score, 2)
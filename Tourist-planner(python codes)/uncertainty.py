def adjust_for_traffic_and_weather(time, traffic, weather):
    extra_time = 0

    if traffic.lower() == "heavy":
        extra_time += 30
    elif traffic.lower() == "medium":
        extra_time += 15

    if weather.lower() == "rainy":
        extra_time += 20
    elif weather.lower() == "cloudy":
        extra_time += 10

    final_time = time + extra_time

    return final_time, extra_time
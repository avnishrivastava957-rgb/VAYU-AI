def weather_agent(state):

    print("🌦️ Weather Agent is running...")

    weather_data = {
        "temperature": 24,
        "humidity": 78,
        "wind_speed": 2.1,
        "rainfall": 0,
        "pressure": 1012
    }

    state["weather"] = weather_data

    return state

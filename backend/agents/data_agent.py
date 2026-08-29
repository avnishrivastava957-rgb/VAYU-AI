def data_quality_agent(state):

    print("🔍 Data Quality Agent is checking the data...")

    weather = state.get("weather", {})
    pollution = state.get("pollution", {})

    missing_weather = [
        key for key, value in weather.items()
        if value is None
    ]

    missing_pollution = [
        key for key, value in pollution.items()
        if value is None
    ]

    state["data_quality"] = {
        "weather_missing": missing_weather,
        "pollution_missing": missing_pollution,
        "status": "Good"
    }

    return state

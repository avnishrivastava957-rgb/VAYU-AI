def pollution_agent(state):

    print("🏭 Pollution Agent is running...")

    pollution_data = {
        "PM2.5": 180,
        "PM10": 290,
        "NO2": 65,
        "SO2": 20,
        "CO": 1.4,
        "O3": 35
    }

    state["pollution"] = pollution_data

    return state

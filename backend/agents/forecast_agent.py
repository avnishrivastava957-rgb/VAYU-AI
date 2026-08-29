def forecast_agent(state):

    print("🧠 Forecast Agent is running...")

    # Temporary prediction for testing.
    # Later, this will be replaced by our trained ML model.

    predicted_pm25 = 210

    state["forecast"] = {
        "predicted_pm25": predicted_pm25,
        "forecast_hours": 24,
        "model": "Temporary"
    }

    return state

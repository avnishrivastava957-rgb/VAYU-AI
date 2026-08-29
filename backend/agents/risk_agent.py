def risk_agent(state):

    print("🚨 Risk Agent is analyzing pollution risk...")

    forecast = state.get("forecast", {})
    pm25 = forecast.get("predicted_pm25", 0)

    if pm25 <= 30:
        risk = "Low"
    elif pm25 <= 60:
        risk = "Moderate"
    elif pm25 <= 90:
        risk = "High"
    else:
        risk = "Very High"

    state["risk"] = {
        "pm25": pm25,
        "risk_level": risk
    }

    return state

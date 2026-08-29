def recommendation_agent(state):

    print("💡 Recommendation Agent is running...")

    risk = state.get("risk", {})
    risk_level = risk.get("risk_level", "Unknown")

    if risk_level == "Low":
        recommendation = "Air quality is good. Normal outdoor activities are safe."

    elif risk_level == "Moderate":
        recommendation = "Sensitive people should reduce prolonged outdoor exposure."

    elif risk_level == "High":
        recommendation = "Reduce outdoor activities and consider wearing a mask outdoors."

    else:
        recommendation = "Avoid unnecessary outdoor activities. Keep windows closed and use air purification if available."

    state["recommendation"] = recommendation

    return state

from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.weather_agent import weather_agent
from agents.pollution_agent import pollution_agent
from agents.data_agent import data_quality_agent
from agents.forecast_agent import forecast_agent
from agents.risk_agent import risk_agent
from agents.recommendation_agent import recommendation_agent


class VayuState(TypedDict, total=False):
    weather: dict
    pollution: dict
    data_quality: dict
    forecast: dict
    risk: dict
    recommendation: str


def build_workflow():

    workflow = StateGraph(VayuState)

    # Add our AI agents
    workflow.add_node("weather", weather_agent)
    workflow.add_node("pollution", pollution_agent)
    workflow.add_node("data_quality", data_quality_agent)
    workflow.add_node("forecast", forecast_agent)
    workflow.add_node("risk", risk_agent)
    workflow.add_node("recommendation", recommendation_agent)

    # Define the agent workflow
    workflow.add_edge(START, "weather")
    workflow.add_edge("weather", "pollution")
    workflow.add_edge("pollution", "data_quality")
    workflow.add_edge("data_quality", "forecast")
    workflow.add_edge("forecast", "risk")
    workflow.add_edge("risk", "recommendation")
    workflow.add_edge("recommendation", END)

    return workflow.compile()


vayu_app = build_workflow()

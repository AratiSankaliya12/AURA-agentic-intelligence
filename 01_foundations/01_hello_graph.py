from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    message: str


def greeting_node(state: AgentState):
    print("Processing greeting node...")
    return {"message": state["message"] + " - Processed by Dhamu's Agent"}


workflow = StateGraph(AgentState)

workflow.add_node("greeting", greeting_node)
workflow.add_edge(START, "greeting")
workflow.add_edge("greeting", END)

app = workflow.compile()

if __name__ == "__main__":
    initial_state = {"message": "Hello, Dhamu's Agent!"}
    result = app(initial_state)
    print("Final Result:", result)

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END


# 1. Define the State
class AgentState(TypedDict):
    user_type: str
    response: str


# 2. Define the Nodes
def receptionist_node(state: AgentState):
    print("Receptionist: Checking ID... ")
    return {"user_type": state["user_type"], "response": "Welcome to the building!"}


def vip_lounge_node(state: AgentState):
    print("VIP Lounge: Providing exclusive access... ")
    return {"user_type": state["user_type"], "response": "Enjoy the VIP lounge!"}


def guest_room_node(state: AgentState):
    print("Guest Room: Providing standard access... ")
    return {
        "user_type": state["user_type"],
        "response": "Enjoy your stay in the guest room!",
    }


# 3. Define the Router (The Security Guard)
def router(state: AgentState) -> Literal["vip_lounge", "guest_room"]:
    print("Security Guard: Routing based on user type... ")
    if state["user_type"] == "VIP":
        return "vip"
    else:
        return "guest"


# 4. Build the Graph
workflow = StateGraph(AgentState)

workflow.add_node("receptionist", receptionist_node)
workflow.add_node("vip_lounge", vip_lounge_node)
workflow.add_node("guest_room", guest_room_node)

# 5. Define the Flow
workflow.add_edge(START, "receptionist")

# Add the crossroad with the router
workflow.add_conditional_edges(
    "receptionist",
    router,
    {
        "vip": "vip_lounge",
        "guest": "guest_room",
    },
)

workflow.add_edge("vip_lounge", END)
workflow.add_edge("guest_room", END)

app = workflow.compile()

# Test the VIP path

print("Testing VIP Path:")
app.invoke({"user_type": "VIP", "response": ""})

print("\nTesting Guest Path:")
app.invoke({"user_type": "Guest", "response": ""})

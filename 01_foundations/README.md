# Phase 1: LangGraph Foundations 🏗️

This phase marks the beginning of **Project AURA**. The goal is to master the core primitives of LangGraph before moving into complex multi-agent orchestration.

## 🎯 Learning Objectives

- **State Management:** Understanding how a `TypedDict` acts as the shared memory (the "Clipboard").
- **Node Design:** Creating functional units that process and update the state.
- **Graph Compilation:** Using `StateGraph` to define the flow of execution.

## 🛠️ The "Hello Graph" Logic

The initial experiment (`01_hello_graph.py`) demonstrates a basic linear workflow:

1. **START** -> Transitions to the `greeter` node.
2. **Greeter Node** -> Appends a custom string to the state message.
3. **END** -> Terminates the execution and returns the final state.

## 🚀 How to Run

Ensure your virtual environment is active, then run:

```bash
python 01_hello_graph.py
```

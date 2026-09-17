from config import llm_con_herramientas
from tools import herramientas

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition


async def nodo_modelo(state: MessagesState) -> dict:
    """Le pasa el historial completo al LLM y devuelve su respuesta (que puede
    incluir tool_calls o ser la respuesta final). """
    respuesta = await llm_con_herramientas.ainvoke(state["messages"])
    return {"messages": [respuesta]}

grafo = StateGraph(MessagesState) #hereda el reducer add_messages
grafo.add_node("modelo", nodo_modelo)
grafo.add_node("herramientas", ToolNode(herramientas, handle_tool_errors=True))

grafo.add_edge(START, "modelo")
grafo.add_conditional_edges(
    "modelo",
    tools_condition,  #mira si el ult mensaje trae tool_calls
    {"tools": "herramientas", END: END},
)
grafo.add_edge("herramientas", "modelo") # el ciclo: vuelve al modelo con el resultado de la tool

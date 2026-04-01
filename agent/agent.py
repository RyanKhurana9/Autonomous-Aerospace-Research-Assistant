import os
from typing import Annotated,TypedDict,Optional,List
from pydantic import BaseModel,Field
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage,HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages#memory manager for conversation state graph
from tools import(
    search_arxiv,
    get_nasa_data,
    rocket_exhaust_velocity,
    reynolds_number,
    calculate_drag_forece,
    calculate_orbital_period,
    calcualte_thrust_to_weight_ratio,
    propellant_mass_flow,
    calculate_mach_Number,
    clauclate_propulsion_efficiency,
    get_ISS_location,
    calculate_orbital_period,
)




 

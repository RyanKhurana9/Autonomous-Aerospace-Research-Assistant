from dotenv import load_dotenv
load_dotenv()
from langchain_ollama import ChatOllama
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
from langchain.memory import ConversationBufferMemory
from tools import search_arxiv,get_nasa_data,rocket_exhaust_velocity
model=ChatOllama(model="llama3.2",temperature=0.7)
tools=[search_arxiv,get_nasa_data,rocket_exhaust_velocity]
# extract predefined prompts from hub
prompts=hub.pull("hwchase17/react-chat")
# create memory object to store conversation history
memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
# create agent using the React framework
agent=create_react_agent(llm=model,tools=tools,prompt=prompts)
#create executor to run the agent
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5,
    memory=memory
)

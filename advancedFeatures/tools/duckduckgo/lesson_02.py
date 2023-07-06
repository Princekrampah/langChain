from langchain.tools import DuckDuckGoSearchRun
from decouple import config
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.agents import initialize_agent, Tool

llm = ChatOpenAI(openai_api_key=config("OPANAI_API_KEY"))

duckduckgo_tool = DuckDuckGoSearchRun()

tools: list = [
    Tool(
        name="DuckDuckGoTool",
        description="Useful when you want to search for information online using duckduckgo. Also useful for general information search online",
        func=duckduckgo_tool.run
    )
]


# creating agent
agent_chain = initialize_agent(
    tools=tools, llm=llm, verbose=True, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

agent_chain.run("What was the historic name of Ghana?")

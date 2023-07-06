from decouple import config
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
import os

# get env in place
os.environ["OPENWEATHERMAP_API_KEY"] = config("OPENWEATHERMAP_API_KEY")

# create LLM
llm = OpenAI(temperature=0, openai_api_key=config("OPANAI_API_KEY"))

# load tools
tools = load_tools(["openweathermap-api"], llm)

agent_chain = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False
)


print(agent_chain.run("What is the weather currently in Nairobi?"))

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from decouple import config


llm = OpenAI(openai_api_key=config("OPANAI_API_KEY"), temperature=0.6)

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("My monthly salary is 10000 KES, if i work for 10 months. How much is my total salary in USD in those 10 months.")

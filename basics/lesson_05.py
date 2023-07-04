from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
from decouple import config
# create LLM model
llm = OpenAI(temperature=0, openai_api_key=config("OPANAI_API_KEY"))


# specify tools you want to use
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# initialize the agent
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


# run agent
agent_result = agent.run(
    "What was the lowest temperature in Nairobi yesterday in Fahrenheit?")

print(agent_result)


# more reading
# https://gist.github.com/geoffreylitt/b345e5a3fcc18368df04b49f6924c217

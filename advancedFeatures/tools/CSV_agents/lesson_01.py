from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent
from decouple import config

llm = ChatOpenAI(openai_api_key=config(
    "OPANAI_API_KEY"), model="gpt-3.5-turbo-0613")

csv_agent = create_csv_agent(llm=llm, path="data.csv", verbose=True,
                             agent_type=AgentType.OPENAI_FUNCTIONS)


# csv_agent.run("What is the average salary of all employees?")

# csv_agent.run("What is the most common recruitment source?")

csv_agent.run("What is the most common race?")



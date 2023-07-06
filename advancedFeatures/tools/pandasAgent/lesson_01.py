from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
import pandas as pd
from decouple import config


df = pd.read_csv("data.csv")

chat_model = ChatOpenAI(openai_api_key=config("OPANAI_API_KEY"))

pd_agent: create_pandas_dataframe_agent = create_pandas_dataframe_agent(
    llm=chat_model,
    # You can provide a list of dataframes if you want: [df, df1]
    df=df,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
)

pd_agent.run("What is the average salary of employees in IT department?")

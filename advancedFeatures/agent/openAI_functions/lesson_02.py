from langchain import LLMMathChain, OpenAI, SerpAPIWrapper, SQLDatabase, SQLDatabaseChain
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from decouple import config
# Planner, Executor and Agent
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner

# create LLM model
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",
                 openai_api_key=config("OPANAI_API_KEY"))
# create a search tool
search = SerpAPIWrapper()
# create an LLM math tool
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
# connect to our database
db = SQLDatabase.from_uri("sqlite:///product_db.db")
# create the database chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

tools = [
    Tool(
        name="SearchTool",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions"
    ),
    Tool(
        name="MathTool",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
    Tool(
        name="Product_Database",
        func=db_chain.run,
        description="useful for when you need to answer questions about products."
    )
]

# planner
planner = load_chat_planner(llm=llm)

# executor
executor = load_agent_executor(llm=llm, tools=tools, verbose=True)

# agent
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

# ask the LLM a question
agent.run("What is the price of the most expensive product? the currency in KES, I want the answer in USD. Convert the currencies to USD")

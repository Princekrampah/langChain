from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
# import for agent creation
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from decouple import config


def my_profile(att: str):
    """Function to return an aspect of my profile"""
    profile_details: dict = {
        "first_name": "John",
        "second_name": "Doe",
        "email": "john@doe.com",
        "age": 34,
        "residence": "Nairobi",
        "street": "Street xyz"
    }

    return profile_details.get(att)


class MyProfileInput(BaseModel):
    """Inputs for my_profile function"""
    attribute: str = Field(description="Attribute of profile detail")


class MyProfileTool(BaseTool):
    name = "my_profile"
    description = """
        Useful when you want to get profile details of John Doe.
        You should enter the attribute of the profile information you want
        """
    args_schema: Type[BaseModel] = MyProfileInput

    def _run(self, attribute: str):
        profile_detail_attribute = my_profile(attribute)
        return profile_detail_attribute

    def _arun(self, attribute: str):
        raise NotImplementedError(
            "my_profile does not support async calls")


llm = ChatOpenAI(
    temperature=0, model="gpt-3.5-turbo-0613",
    openai_api_key=config("OPANAI_API_KEY")
)

tools = [
    MyProfileTool()
]

agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

agent.run("Where does John Doe reside")

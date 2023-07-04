#### Chat Models ####
from decouple import config

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
# import PromptTemplate
from langchain.prompts import PromptTemplate

chat_model: ChatOpenAI = ChatOpenAI(openai_api_key=config("OPANAI_API_KEY"))

prediction_msg: dict = chat_model.predict_messages(
    [HumanMessage(content="When was the end of the first world war?"), SystemMessage(content="Talk like you are a German, keep your responses below 50 words but more than 40 words.")])

print(prediction_msg)
print(prediction_msg.content)

from langchain import OpenAI, ConversationChain
from decouple import config
import time

llm = OpenAI(temperature=0, openai_api_key=config("OPANAI_API_KEY"))

# Conversation
conversation = ConversationChain(
    llm=llm,
    verbose=True
)

conversation.run("How are you doing today?")
time.sleep(10)
conversation.run("I would like to know what is the largest country on Earth.")
time.sleep(10)
conversation.run("Thank you and have a good day.")


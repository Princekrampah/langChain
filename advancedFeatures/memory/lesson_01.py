from langchain.chains import LLMChain
from langchain import OpenAI
from langchain.memory import ConversationBufferMemory
from decouple import config
from langchain.prompts import PromptTemplate
import time

llm = OpenAI(temperature=0, openai_api_key=config("OPANAI_API_KEY"))

template = """You are a chatbot having a conversation with a human.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

# Conversation
llm_chain = LLMChain(
    llm=OpenAI(),
    prompt=prompt,
    verbose=True,
    memory=memory,
)


llm_chain.run("How are you doing today?")
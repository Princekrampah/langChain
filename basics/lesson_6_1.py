from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import time

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Your name is hilda, you are a historian, very talkative and smart "
        "Answer the questions you are being asked and have a sense of humour "
        "You should be kind and polite in your responses"
    ),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

conversation.predict(input="Hi there!")
time.sleep(5)
conversation.predict(
    input="Can you tell me about the history of the first world war, who are the winners you think?")
time.sleep(5)
conversation.predict(input="Hi there!")

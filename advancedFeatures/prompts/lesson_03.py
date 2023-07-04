#### Chat models with Prompts ####
from decouple import config
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate

# Create the first prompt template
sys_prompt: PromptTemplate = PromptTemplate(
    input_variables=["original_sentence", "desired_language"],
    template="""You are a language translater, an English speaker wants to translate/
    {original_sentence} to {desired_language}. Tell him the corrent answer."""
)

system_message_prompt = SystemMessagePromptTemplate(prompt=sys_prompt)

student_prompt: PromptTemplate = PromptTemplate(
    input_variables=["original_sentence", "desired_language"],
    template="Translate {original_sentence} to {desired_language}"
)
student_message_prompt = HumanMessagePromptTemplate(prompt=student_prompt)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, student_message_prompt])

# create the chat model
chat_model: ChatOpenAI = ChatOpenAI(openai_api_key=config("OPANAI_API_KEY"))


# Create the LLM chain
chain: LLMChain = LLMChain(llm=chat_model, prompt=chat_prompt)

# make a call to the models
prediction_msg: dict = chain.run(
    original_sentence="I love Pizza!", desired_language="French")

print("#######################################")
print(prediction_msg)
print("#######################################")

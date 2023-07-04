#### Chains wiht Chat models ####
#### Chat models with Prompts ####
from decouple import config
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

sys_template: str = """You are a language translater, an English speaker wants to translate {original_sentence} to {desired_language}. Tell him the corrent answer."""
system_message_prompt = SystemMessagePromptTemplate.from_template(sys_template)

student_template = "Translate {original_sentence} to {desired_language}"
student_message_prompt = HumanMessagePromptTemplate.from_template(
    student_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, student_message_prompt])

# we do not longer need this anymore
# chat_prompt_format = chat_prompt.format_messages(
#     original_sentence="I love Pizza!", desired_language="French")
# print(chat_prompt_format)

chat_model: ChatOpenAI = ChatOpenAI(openai_api_key=config("OPANAI_API_KEY"))

# we do not need this any more
# prediction_msg: dict = chat_model.predict_messages(messages=chat_prompt_format)

# Create the LLM chain
chain: LLMChain = LLMChain(llm=chat_model, prompt=chat_prompt)

prediction_msg: dict = chain.run(
    original_sentence="I love Pizza!", desired_language="French")

print("#######################################")
print(prediction_msg)
print("#######################################")

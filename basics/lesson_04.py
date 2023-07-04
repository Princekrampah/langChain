#### Prompts ####
from decouple import config
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# import PromptTemplate
from langchain.prompts import PromptTemplate

llm = OpenAI(openai_api_key=config("OPANAI_API_KEY"))


prompt = PromptTemplate.from_template(
    "What is the name of the capital city of {country}?")

# we do not need this any more
# prompt_formatted_str: str = prompt.format(country="United States")
# print(prompt_formatted_str)

chain = LLMChain(llm=llm, prompt=prompt)
prediction: str = chain.run(country="United States")

print(prediction)
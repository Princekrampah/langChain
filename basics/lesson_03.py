#### Prompts ####
from decouple import config
from langchain.llms import OpenAI

# import PromptTemplate
from langchain.prompts import PromptTemplate

llm = OpenAI(openai_api_key=config("OPANAI_API_KEY"))


prompt = PromptTemplate.from_template(
    "What is the name of the capital city of {country}?")
prompt_formatted_str: str = prompt.format(country="United States")


print(prompt_formatted_str)

prediction: str = llm.predict(prompt_formatted_str)

print(prediction)

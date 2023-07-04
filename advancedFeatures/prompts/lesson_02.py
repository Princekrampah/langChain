#### Generating Prompt templates Efficiently ####
from langchain.llms import OpenAI
# decouple to read .env variables(OpenAI Key)
from decouple import config
# import openAI from langChain
from langchain.llms import OpenAI
# import prompt template
from langchain import PromptTemplate

# create the prompt, here we use multiple inputs
prompt = PromptTemplate(
    template=""""/
You are a vehicle mechanic, give responses to the following/ 
question: {question}. Do not use technical words, give easy/
to understand responses. Your response should be in {language}""",
    input_variables=["question", "language"]
)

# format the prompt to add variable values
prompt_formatted_str: str = prompt.format(
    question="Why won't a vehicle start on ignition?",
    language="Spanish")

# instantiate the OpenAI intance
llm = OpenAI(openai_api_key=config("OPANAI_API_KEY"))

# make a prediction
prediction = llm.predict(prompt_formatted_str)

# print the prediction
print(prediction)

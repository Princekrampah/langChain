from langchain.llms import OpenAI
# decouple to read .env variables(OpenAI Key)
from decouple import config
# import openAI from langChain
from langchain.llms import OpenAI

# instantiate the OpenAI intance
llm = OpenAI(openai_api_key=config("OPANAI_API_KEY"))

# make a prediction
prediction = llm.predict("What is the largest city in Africa?")

# print the prediction
print(prediction)


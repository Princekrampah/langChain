from langchain.chains import TransformChain, LLMChain, SimpleSequentialChain
from langchain.prompts import PromptTemplate
# for creating LLM
from langchain.llms import OpenAI
# decouple to read .env variables(OpenAI Key)
from decouple import config

# read file
with open("./data.txt", "r") as file:
    # print(file.read())
    file_content: str = file.read()


def transform_func(data: dict) -> dict:
    text_data: str = data["text"]
    file_content: str = text_data.replace("Hello world", "Hello people")
    return {"output_text": file_content}


transform_chain = TransformChain(
    input_variables=["text"], output_variables=["output_text"], transform=transform_func
)

template = """What people are being greeted in the text:

{output_text}

Summary:"""

prompt = PromptTemplate(input_variables=["output_text"], template=template)

# create LLM
llm = OpenAI(openai_api_key=config("OPANAI_API_KEY"))
llm_chain = LLMChain(llm=llm, prompt=prompt)

# create a simple sequential chain
sequential_chain = SimpleSequentialChain(chains=[transform_chain, llm_chain])

# run
result: str = sequential_chain.run(file_content)
print(result)
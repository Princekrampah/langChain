import asyncio
import time

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from decouple import config


OpenAI.openai_api_key = config("OPANAI_API_KEY")

def generate_serially():
    llm = OpenAI(temperature=0.9, openai_api_key=config("OPANAI_API_KEY"))
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    for _ in range(5):
        resp = chain.run(product="toothpaste")
        print(resp)


async def async_generate(chain):
    resp = await chain.arun(product="toothpaste")
    print(resp)
    return resp


async def generate_concurrently():
    llm = OpenAI(temperature=0.9, openai_api_key=config("OPANAI_API_KEY"))
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    tasks = [async_generate(chain) for _ in range(5)]
    await asyncio.gather(*tasks)


s = time.perf_counter()

asyncio.run(generate_concurrently())


elapsed = time.perf_counter() - s
print("\033[1m" +
      f"Concurrent executed in {elapsed:0.2f} seconds." + "\033[0m")

s = time.perf_counter()
generate_serially()
elapsed = time.perf_counter() - s
print("\033[1m" +
      f"Serial executed in {elapsed:0.2f} seconds." + "\033[0m")




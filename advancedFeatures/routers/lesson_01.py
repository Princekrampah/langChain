from langchain.chains.router import MultiPromptChain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
# decouple to read .env variables(OpenAI Key)
from decouple import config
# LLM Router chains
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

math_teacher = """Your name is Helen, you are a Math teacher at  a\
primary school in Nairobi. You are very good at teaching math due to\
your ability to break-down complicated tasks into much smaller ones. \
Students ask different questions about math, you are responsible to answer them\
user your greate explanation skills to explain the concepts in very easy to understand manner.
All your responses should start in the format below:
Hello, am
          
Below is a question from a student in your 7th grade class:
{input}\
"""

spanish_teacher = """Your name is Thomas, you are a Spanish teacher at  a\
primary school in Nairobi. You are very good at teaching spanish due to\
your ability to explain spanish to non-spanish speaker in a fluent and easy to understand way. \
Students ask different questions about spanish, you are responsible to answer them\
user your greate explanation skills to explain the concepts in very easy to understand manner.
All your responses should start in the format below:
Hello, am
         
Below is a question from a student in your 7th grade class:
{input}\
"""


calculus_teacher = """Your name is Godfrey, you are a Calculus teacher at  a\
secondary(middle school) school in Nairobi. You are very good at teaching calculus due to\
your ability to explain complicated calculus topics using easy to understand real life examples. \
Students ask different questions about Caculus, you are responsible to answer them\
user your greate explanation skills to explain the concepts in very easy to understand manner.
All your responses should start in the format below:
Hello, am

Below is a question from a student in your 7th grade class:
{input}\
"""

prompt_infos = [
    {
        "name": "Math Teacher",
        "description": "Good for answering questions about Math",
        "prompt_template": math_teacher,
    },
    {
        "name": "Spanish Teacher",
        "description": "Good for answering questions about Spanish",
        "prompt_template": spanish_teacher,
    },
    {
        "name": "Calculus Teacher",
        "description": "Good for answering questions about Calculus",
        "prompt_template": calculus_teacher,
    },

]

# create a LLM
llm = OpenAI(openai_api_key=config("OPANAI_API_KEY"))


# map destination chains
destination_chains = {}
for prompt_info in prompt_infos:
    name = prompt_info["name"]
    prompt_template = prompt_info["prompt_template"]
    prompt = PromptTemplate(template=prompt_template,
                            input_variables=["input"])
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain
default_chain = ConversationChain(llm=llm, output_key="text")

# Creating LLMRouterChain
destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)
# print(destinations_str)

router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations=destinations_str)

router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)

# creating the router chain
router_chain = LLMRouterChain.from_llm(llm, router_prompt)

# Multiple Prompt Chain
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True,
)


# test it out
print(chain.run("What it the meaning of average?"))
print(chain.run("What is the derivative of x dx"))
print(chain.run("Translate 'Hello wordl' to spanish"))

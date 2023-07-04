#### Prompt Validation ####
from langchain.prompts import PromptTemplate, StringPromptTemplate
import pandas as pd

from langchain.llms import OpenAI
# decouple to read .env variables(OpenAI Key)
from decouple import config
# import openAI from langChain
from langchain.llms import OpenAI
# import prompt template
from langchain import PromptTemplate
# validator and Basemodels import
from pydantic import BaseModel, validator

# prompt template
template = """Given the an employee's up to date stats, write them note relaying those stats to them.
Give me a full description of the employee's recruitment source, thier salary and race, if they have a 
special projects count of more than 5 congratulate them on it. Your name is Helen and you work in HR.Place the employee 
details in a tabular format as well.

Here are the employee stats:
recruitment source: {recruitment_source}
salary in Ksh: {salary}
special projects count: {special_projects_count}
race: {race_desc}
department: {department}
Employee name:{employee_name}

Your response:"""
prompt = PromptTemplate.from_template(template)


# class to filter data and pass the information into
# the prompt template we have above.
class DBPromptTemplate(StringPromptTemplate):
    @validator("input_variables")
    def validate_input_variables(cls, v):
        """Validate that the input variables are correct."""

        # we want to make sure we have exactly 5 input variables
        if len(v) != 5:
            raise ValueError("Make sure your input_variables are correct.")
        return v

    def format(self, **kwargs) -> str:
        employee_id = kwargs.pop("EmpID")
        df = pd.read_csv("./data.csv")
        row = df[df["EmpID"] == int(employee_id)]
        kwargs["recruitment_source"] = row["RecruitmentSource"].values[0]
        kwargs["salary"] = row["Salary"].values[0]
        kwargs["race_desc"] = row["RaceDesc"].values[0]
        kwargs["department"] = row["Department"].values[0]
        kwargs["special_projects_count"] = row["SpecialProjectsCount"].values[0]
        kwargs["employee_name"] = row["Employee_Name"].values[0]
        return prompt.format(**kwargs)

    def _prompt_type(self):
        return "employee_stats"


employee_stats = DBPromptTemplate(input_variables=[
    "recruitment_source", "salary", "special_projects_count", "race_desc", "department"])
employee_stats = employee_stats.format(EmpID=10084)
# print(employee_stats)


# instantiate the OpenAI intance
llm = OpenAI(openai_api_key=config("OPANAI_API_KEY"))

# make a prediction
prediction = llm.predict(employee_stats)

# print the prediction
print(prediction)

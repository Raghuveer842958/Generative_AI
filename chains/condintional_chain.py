from langchain_groq import ChatGroq
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model1 = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.5,
)

model2 = ChatOpenRouter(
    model = "openai/gpt-4o-mini",
    temperature = 0.5,
)

parser1 = StrOutputParser()

class FeedBack(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the followint review")

parser2 = PydanticOutputParser(pydantic_object=FeedBack)

prompt1 = PromptTemplate(
    template="classify the sentiment of the following feedback text into positive or negative -> \n {feedback}", 
    input_variables=["feedback"],
)

prompt2 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

calssifier_chain = prompt2 | model2 | parser2

result = calssifier_chain.invoke({"feedback": "Pizza was yummy"})

print("cassifier result is :", result)

prompt3 = PromptTemplate(
    template="write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt4 = PromptTemplate(
    template="write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt3 | model2 | parser1),
    (lambda x:x.sentiment == 'negative', prompt4 | model2 | parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = calssifier_chain | branch_chain

result = chain.invoke({"feedback": "This is the beautiful phone"})

print("final result is :", result)
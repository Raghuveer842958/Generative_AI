from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.5,
)

parser = StrOutputParser()

topic_prompt = PromptTemplate(
    template="Generate a detailed report about the {topic}", 
    input_variables=["topic"]
)

summary_prompt = PromptTemplate(
    template="give me 5 key points about the following report: {report}",
    input_variables=["report"]
)

topic = input("Enter a topic : ")

chain = topic_prompt | model | parser | summary_prompt | model | parser
chain.get_graph().print_ascii()

result = chain.invoke({"topic": topic})

print("final result :", result)
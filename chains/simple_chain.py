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

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}.",
    input_variables=["topic"]
)

topic = input("Enter a topic to generate interesting facts about: ")

chain = prompt | model | parser
chain.get_graph().print_ascii()

result = chain.invoke({"topic": topic})

print("Interesting facts about", topic, ":\n", result )


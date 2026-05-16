from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# model = ChatGroq()
# model = ChatOpenAI()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.5,
)

template1 = PromptTemplate(
    template="Generate a brief report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
)

topic = input("Enter a topic to learn about: ")

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic": topic})
# result = model.invoke(template1.format(topic=topic))

# text = result.content
print("result is :", result)

print("***************************************************")
# summary = model.invoke(template2.format(text=text))
# chain2 = template2 | model
# summary = chain2.invoke({"text": text})
# print("summary is :", summary.content)

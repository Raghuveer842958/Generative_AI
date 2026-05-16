from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

load_dotenv()

# model = ChatGroq()
# model = ChatOpenAI()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.5,
)

parser = JsonOutputParser()

template1 = PromptTemplate(
    template="Generate a brief report on {topic}",
    input_variables=["topic"]
)

# template2 = PromptTemplate(
#     template="Write a 5 line summary on the following text. /n {text} \n Format the output in JSON",
#     input_variables=["text"]
# )

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text} \n {format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

print("template2 is :--", template2)

topic = input("Enter a topic to learn about: ")

chain = template1 | model | template2 | model
result = chain.invoke({"topic": topic})
# result = model.invoke(template1.format(topic=topic))

# text = result.content
print("result is :", parser.parse(result.content))

print("***************************************************")
# summary = model.invoke(template2.format(text=text))
# chain2 = template2 | model
# summary = chain2.invoke({"text": text})
# print("summary is :", summary.content)

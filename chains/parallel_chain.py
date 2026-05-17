from langchain_groq import ChatGroq
from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.5,
)

model2 = ChatOpenRouter(
    model = "openai/gpt-4o-mini",
    temperature = 0.5,
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a sort report about the {topic}", 
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="give me 5 questions and answers about the given text -> {topic}",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template = "merge the provided notes and queze into single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables = ['notes', 'quiz']
)

topic = input("Enter a topic : ")

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'topic': topic})

chain.get_graph().print_ascii()

print("final result :", result)
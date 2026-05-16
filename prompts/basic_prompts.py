from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3",
    temperature = 0.5,
    task = "text-generation",
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Tell me about {topic}",
    input_variables=["topic"]
)

user_topic = input("Enter a topic to learn about: ")

PromptResult = prompt.invoke({"topic": user_topic})
result = model.invoke(PromptResult)
print("Prompt is :",PromptResult)
print("AI response is :",result.content)
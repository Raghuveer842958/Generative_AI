from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3",
    temperature = 0.5,
    task = "text-generation",
)
model = ChatHuggingFace(llm=llm)

# prompt = PromptTemplate(
#     template="Explain {topic} in {language}",
#     input_variables=["topic", "language"]
# )

prompt = load_prompt(".\prompts\prompt_template.json")

user_topic = input("Enter a topic to learn about: ")
user_language = input("Enter a language to explain in: ")

chain = prompt | model

prompt_result = prompt.invoke({"topic": user_topic, "language": user_language})
print("Prompt is :",prompt_result)
result = model.invoke(prompt_result)
# result = chain.invoke({"topic": user_topic, "language": user_language})
print("AI response is :",result.content)
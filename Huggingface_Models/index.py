from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# 1. deepseek-ai/DeepSeek-V3
# 2. mistralai/Mistral-7B-Instruct-v0.3

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-7B-Instruct",
    temperature = 0.5,
    task = "text-generation",
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("explain React hooks simply")

print("AI response is :",result.content)

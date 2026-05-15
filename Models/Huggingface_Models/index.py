from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# 1. deepseek-ai/DeepSeek-V3
# 2. mistralai/Mistral-7B-Instruct-v0.3


llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    temperature = 0.5,
    task = "text-generation",
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("explain React hooks simply")

print("AI response is :",result.content)

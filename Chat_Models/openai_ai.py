from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0.5,
    max_completion_tokens = 50
)

result = model.invoke("explain what is the agentic ai in simple words and keep it short as possible")

print("AI response is :",result)
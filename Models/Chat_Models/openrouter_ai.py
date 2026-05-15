from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenRouter(
    model = "openai/gpt-4o-mini",
    temperature = 0.5,
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love Cricket."),
]

result = model.invoke(messages)

print("Ai response:--", result.content)
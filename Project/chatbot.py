from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, load_prompt
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3",
    temperature = 0.5,
    task = "text-generation",
)

llm = ChatHuggingFace(llm=model)

chat_history = [
    SystemMessage(content="you are a helpfull assistant"),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break

    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)


print("Chat history: ", chat_history)
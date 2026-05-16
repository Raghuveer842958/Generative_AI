from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ("system", "you are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{query}"),
])

chat_history = []

with open('./prompts/history.txt') as f:
    chat_history.extend(f.readlines())

print("chat history: ",chat_history)

user_query = input("Enter your query: ")

prompt = chat_template.invoke({"history": chat_history, "query": user_query})
print("Prompt is: ", prompt)
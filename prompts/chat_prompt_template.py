from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} assistant."),
    ("human", "What is {topic}? Explain in simple terms.")
])

prompt = chat_template.invoke({
    "domain": "React.js",
    "topic": "Hooks"
})

print(prompt)
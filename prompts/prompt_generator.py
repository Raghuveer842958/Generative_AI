from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="Explain {topic} in {language}",
    input_variables=["topic", "language"]
)

prompt.save(".\prompts\prompt_template.json")
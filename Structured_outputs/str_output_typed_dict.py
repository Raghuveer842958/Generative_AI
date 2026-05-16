from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

# model = HuggingFaceEndpoint(
#     repo_id = "deepseek-ai/DeepSeek-V3",
#     temperature = 0.5,
#     task = "text-generation",
# )

# llm = ChatHuggingFace(llm=model)

# llm = ChatOpenAI(
#     model = "gpt-4o-mini",
#     temperature = 0.5,
# )

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.5,
)

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review in 1-2 sentences"]
    sentiment: Annotated[Literal["pos", "neg", "neu"], "The sentiment of the review, either 'positive', 'negative', or 'neutral'"]
    key_themes: Annotated[list[str], "A list of key themes mentioned in the review, such as 'battery life', 'performance', 'design', etc."]
    pros: Annotated[Optional[list[str]], "A list of pros mentioned in the review, if any. If no pros are mentioned, this should be None."]
    cons: Annotated[Optional[list[str]], "A list of cons mentioned in the review, if any. If no cons are mentioned, this should be None."]
    name: Annotated[Optional[str], "The name of the reviewer, if mentioned in the review. If no name is mentioned, this should be None."]

structured_output = llm.with_structured_output(Review)

result = structured_output.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Raghu
""")


print("result is :", result)
print("Summary:", result['summary'])
print("Sentiment:", result['sentiment'])
print("Key Themes:", result['key_themes'])
print("Pros:", result['pros'])
print("Cons:", result['cons'])
print("Name:", result['name'])
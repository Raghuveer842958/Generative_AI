from openai import OpenAI
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Create client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Send request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "What is the capital city of India?"
        }
    ]
)

# Print response
print(response.choices[0].message.content)
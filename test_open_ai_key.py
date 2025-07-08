import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Set your API key
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])  # or hardcode it directly

# Minimal input (only ~3 tokens)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Hi"}
    ],
    max_tokens=10  # Small output to keep cost near zero
)

print("Response:", response.choices[0].message.content)

import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# Set your OpenAI API key
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])  # or hardcode it for quick testing

# Tiny test input
test_text = "Hello world"

# Call the embedding model
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=test_text
)

# Output the embedding vector length (should be 1536 or similar)
embedding = response.data[0].embedding
print("Embedding length:", len(embedding))
print("First 5 values:", embedding[:5])

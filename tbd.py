import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#initialize client with API key from .env
client = OpenAI(
  api_key = os.getenv('OPENAI_API_KEY'),
)

#Starting a chat with GPT3.5
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
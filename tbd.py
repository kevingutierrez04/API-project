import os
from openai import OpenAI
from dotenv import load_dotenv

#new imports
import requests
import pandas as pd
import sqlalchemy as db
import json

load_dotenv()

#initialize client with API key from .env
client = OpenAI(
  api_key = os.getenv('OPENAI_API_KEY'),
)

#Starting a chat with GPT3.5
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={ "type": "json_object"},
    messages=[
      {"role": "system", "content": "You are a helpful assistant designed to output JSON. Surround the value of every JSON value with square brackets"}, 
      {"role": "user", "content": '''
    Give me a one paragraph explanation about the nintendo game Splatoon. 
    '''}],
    
    stream=True,
)
test = ""
for chunk in stream:
  if chunk.choices[0].delta.content:
    test += chunk.choices[0].delta.content
ans = json.loads(test)

for key in ans:
  if isinstance(ans[key], list):
    ans[key] = '. '.join([str(item) for item in ans[key]])

epic = pd.DataFrame.from_dict([ans])
engine = db.create_engine('sqlite:///placeholder.db')
epic.to_sql('Responses', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
  query_result = connection.execute(db.text("SELECT * FROM Responses;")).fetchall()
  print(pd.DataFrame(query_result))
  print(chunk.choices[0].delta.content, end="")
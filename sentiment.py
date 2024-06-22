import requests

url = 'http://text-processing.com/api/sentiment/'

epic = input()

myobj = {
  'text': epic
  }
response = requests.post(url, data = myobj)

print(response.json())


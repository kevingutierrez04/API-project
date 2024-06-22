import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)

print(response.status_code)

data = response.json()

epic = [person['name'] for person in data['people']]

for name in epic[:5]:
  print(name)
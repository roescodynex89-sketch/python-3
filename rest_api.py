import requests


response=requests.get("https://api.mydummyapi.com/comments/1")

data=response.json()
print(data)
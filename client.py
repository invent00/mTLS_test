import requests

url = "https://localhost:8000/"
response = requests.get(url, cert=('client.pem', 'client.key'), verify='ca.pem')

print(response.json())
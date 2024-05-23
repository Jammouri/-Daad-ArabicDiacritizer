import requests
response=requests.get('http://127.0.0.1:8000/jameel/3/8')
print(response.json())

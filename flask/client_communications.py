import requests

data = {}
result = requests.get('http://localhost:5000/addTree', json=data)
print(result)
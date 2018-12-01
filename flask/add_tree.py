import requests

data = {}
result = requests.post('http://localhost:5000/addTree', json=data)
print(result)
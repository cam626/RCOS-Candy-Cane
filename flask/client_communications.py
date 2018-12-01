import requests

data = {'name': 'newTree', 'color': 'blue'}
result = requests.post('http://localhost:5000/addTree', json=data)

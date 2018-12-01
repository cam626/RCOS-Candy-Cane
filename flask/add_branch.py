import requests

data = {'color': 'green', 'width': '50', 'height': '100'}
result = requests.post('http://localhost:5000/modify/addBranch/1', json=data)
print(result)
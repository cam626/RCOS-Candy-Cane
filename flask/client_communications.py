import requests

def sendBranch(treeID, color, width, height):
	data = {'color': color,
			'width': width,
			'height': height}

	url = 'http://localhost:5000/addBranch/' + str(treeID)
	result = requests.post(url, json=data)
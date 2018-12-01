import requests

def getTree(treeID):
	result = requests.get('http://localhost:5000/getTree/' + str(treeID))
	return result.text

def sendBranch(treeID, color, x, y, width, height):
	data = {'color': color,
			'x': x,
			'y': y,
			'width': width,
			'height': height}

	url = 'http://localhost:5000/modify/addBranch/' + str(treeID)
	result = requests.post(url, json=data)

def createTree():
	result = requests.post('http://localhost:5000/addTree')
	return result.text

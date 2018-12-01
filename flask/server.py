from flask import Flask, request
from tree import Tree
app = Flask(__name__)
import json


testTree = Tree()
testTree.background = "black"
trees = {0: testTree}

@app.route('/trees')
def getTrees():
	response = []
	for tree in trees:
		response.append(trees[tree].jsonify())
	return json.dumps(response)

@app.route('/addTree', methods=["POST"])
def addTree():
	newTree = Tree()
	id = max(list(trees.keys()) or [0]) + 1
	print(id)
	trees[id] = newTree
	return str(id)

@app.route('/getTree/<int:treeID>', methods=["GET"])
def getTree(treeID):
	return json.dumps(trees[treeID].jsonify())

@app.route('/modify/addBranch/<int:treeID>', methods=["POST"])
def addBranch(treeID):
	input_json = request.get_json(force=True)
	color = input_json['color']
	width = int(input_json['width'])
	height = int(input_json['height'])
	y = int(input_json['y'])
	x = int(input_json['x'])
	trees[treeID].addBranch(color, x, y, width, height)
	return "Yes"

@app.route('/modify/addOrnament/<int:treeID>', methods=["POST"])
def addOrnament(treeID):
	input_json = request.get_json(force=True)
	color = input_json['color']
	width = int(input_json['width'])
	height = int(input_json['height'])
	y = int(input_json['y'])
	x = int(input_json['x'])
	trees[treeID].addOrnament(color, x, y, width, height)
	return "Yes"

@app.route('/modify/trunk/<int:treeID>', methods=["POST"])
def changeTrunk(treeID):
	input_json = request.get_json(force=True)
	color = input_json['color']
	width = int(input_json['width'])
	height = int(input_json['height'])
	trees[treeID].trunk.color = color
	trees[treeID].trunk.width = width
	trees[treeID].trunk.height = height
	return "Yes"

@app.route('/modify/background/<int:treeID>', methods=["POST"])
def changeTrunk(treeID):
	input_json = request.get_json(force=True)
	color = input_json['color']
	trees[treeID].background = color
	return "Yes"

@app.route('/modify/topper/<int:treeID>', methods=["POST"])
def changeTrunk(treeID):
	input_json = request.get_json(force=True)
	type = input_json['type']
	color = input_json['color']
	trees[treeID].topper.type = type
	trees[treeID].topper.color = color
	return "Yes"
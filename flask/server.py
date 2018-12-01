from flask import Flask, request
app = Flask(__name__)
import json

class Tree(object):
	def __init__(self, name, color):
		self.name = name
		self.color = color

trees = []

@app.route('/trees')
def getTrees():
	response = []
	for tree in trees:
		response.append([tree.name, tree.color])
	return json.dumps(response)

@app.route('/addTree', methods=["POST"])
def addTree():
	input_json = request.get_json(force=True)
	newTree = Tree(input_json['name'], input_json['color'])
	trees.append(newTree)
	return newTree.name
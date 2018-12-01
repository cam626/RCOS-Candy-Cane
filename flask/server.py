from flask import Flask
app = Flask(__name__)
import json
import request

trees = []

@app.route('/trees')
def getTrees():
	response = {'trees':['T1', 'T2']}
	return json.dumps(response)

@app.route('/addTree')
def addTree():
	trees.append(request.args.get('name'))
	return trees[0]
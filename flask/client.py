import sys
import json
import requests

trees = requests.get("http://localhost:5000/trees").json()
print(trees)
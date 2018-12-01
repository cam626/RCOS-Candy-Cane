class Tree:
    def __init__(self):
        self.branches = []
        self.topper = None
        self.background = "white"
        self.ornaments = []
        self.trunk = None
    
class Branch:
    def __init__(self):
        self.color = "green"
        self.width = 50
        self.length = 100

class Topper:
    def __init__(self, type="star"):
        self.type = type

class Ornaments:
    def __init__(self, type="round", color="red"):
        self.type = type
        self.color = color

class Trunk:
    def __init__(self):
        self.color = "brown"
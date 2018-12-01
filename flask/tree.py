class Tree:
    def __init__(self):
        self.branches = []
        self.topper = Topper()
        self.background = "white"
        self.ornaments = []
        self.trunk = Trunk()
        self.lights = []

    def jsonify(self):
        result = {"branches": self.jsonList(self.branches),
                    "topper": self.topper.jsonify(),
                    "background": self.background,
                    "ornaments": self.jsonList(self.ornaments),
                    "lights": self.jsonList(self.lights),
                    "trunk": self.trunk.jsonify()}
        return result

    def addBranch(self, color, x, y, width, height):
        self.branches.append(Branch(color, x, y, width, height))

    def addOrnament(self, color, x, y, width, height):
        self.ornaments.append(Ornament(color, x, y, width, height))

    def addLight(self, color, x, y, width, height):
        self.lights.append(Lights(color, x, y, width, height))

    def jsonList(self, l):
        list_json = "["
        for item in l:
            list_json += item.jsonify()
        list_json += "]"
        return list_json
    
class Branch:
    def __init__(self, color="green", x=0, y=0, width=100, height=50):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def jsonify(self):
        res = "{color:" + self.color + ", x:" + str(self.x) + \
                ", y:" + str(self.y) + ", width:" + str(self.width) + ", height:" + str(self.height) + "}"
        return res

class Topper:
    def __init__(self, type="star", color="yellow"):
        self.type = type
        self.color = color

    def jsonify(self):
        res = "{type:" + self.type + ", color:" + self.color + "}"
        return res

class Ornament:
    def __init__(self, color="red", x=0, y=0, width=25, height=25):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def jsonify(self):
        res = "{color:" + self.color + ", x:" + str(self.x) + \
                ", y:" + str(self.y) + ", width:" + str(self.width) + ", height:" + str(self.height) + "}"
        return res

class Light:
    def __init__(self, color="red", x=0, y=0, width=25, height=25):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def jsonify(self):
        res = "{color:" + self.color + ", x:" + str(self.x) + \
                ", y:" + str(self.y) + ", width:" + str(self.width) + ", height:" + str(self.height) + "}"
        return res

class Trunk:
    def __init__(self, color="brown", width=50, height=100):
        self.color = color
        self.width = width
        self.height = height

    def jsonify(self):
        res = "{color:" + self.color + ", width:" + str(self.width) + ", height:" + str(self.height) + "}"
        return res
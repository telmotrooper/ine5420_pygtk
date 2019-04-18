# pylint: disable=no-name-in-module, import-error
from utils.gen_random_id import generateRandomId
from transform import Transform

class Shape:
  def __init__(self, name):
    self.world_coords = []
    self.normalized_coords = []
    self.name = name
    self.id = generateRandomId()
    self.transform = Transform()

  def addCoords(self, x, y):
    self.world_coords.append({"x": x, "y": y})
    self.normalized_coords.append(self.transform.normalize(x, y))

  def getWorldCoords(self):
    return self.world_coords

  def getNormalizedCoords(self):
    return self.normalized_coords
  
  def scaleNormalizedCoords(self, percentage):
    coords = self.normalized_coords

    for i in range(len(coords)):
      new_coords = self.transform.scale(
        coords[i]["x"], coords[i]["y"],
        percentage, percentage,
        0, 0
      )
      self.normalized_coords[i] = {"x": new_coords[0], "y": new_coords[1]}
  
  def rotateNormalizedCoords(self, degrees):
    coords = self.normalized_coords

    for i in range(len(coords)):
      new_coords = self.transform.rotation(coords[i]["x"], coords[i]["y"], 0, 0, degrees)
      self.normalized_coords[i] = {"x": new_coords[0], "y": new_coords[1]}

  def setWorldCoords(self, i, x, y):
    self.world_coords[i] = { "x": x, "y": y }
    self.normalized_coords[i] = self.transform.normalize(x, y)

  def normalizeCoords(self):
    for i in range(len(self.world_coords)):
      x, y = self.world_coords[i]["x"], self.world_coords[i]["y"]
      self.normalized_coords[i] = self.transform.normalize(x, y)

  def getName(self):
    return self.name

  def getId(self):
    return self.id

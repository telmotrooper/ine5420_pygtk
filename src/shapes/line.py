import numpy as np
# pylint: disable=no-name-in-module, import-error
from utils.gen_random_id import generateRandomId
from transform import Transform

class Line:
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

  def setWorldCoords(self, i, x, y):
    self.world_coords[i] = { "x": x, "y": y }
    self.normalized_coords[i] = self.transform.normalize(x, y)

  def setNormalizedCoords(self, i, x, y):
    self.world_coords[i] = self.transform.denormalize(x, y)
    self.normalized_coords[i] = { "x": x, "y": y }

  def getName(self):
    return self.name

  def getId(self):
    return self.id

  def drawToViewport(self, ctx, viewport):
    x, y = self.normalized_coords[0]["x"], self.normalized_coords[0]["y"]
    x2, y2 = self.normalized_coords[1]["x"], self.normalized_coords[1]["y"]

    point1 = viewport.transform(x, y)
    point2 = viewport.transform(x2, y2)

    ctx.move_to(point1["x"],point1["y"])
    ctx.line_to(point2["x"], point2["y"])
    ctx.stroke()

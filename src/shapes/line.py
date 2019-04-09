import numpy as np
# pylint: disable=no-name-in-module, import-error
from utils.gen_random_id import generateRandomId

class Line:
  def __init__(self, name):
    self.world_coords = []
    self.normalized_coords = []
    self.name = name
    self.id = generateRandomId()
  
  def addCoords(self, x, y):
    self.world_coords.append(
      {"x": x, "y": y}
    )
    self.normalized_coords.append(
      {"x": x, "y": y}
    )

  def getWorldCoords(self):
    return self.world_coords

  def getNormalizedCoords(self):
    return self.normalized_coords

  def getName(self):
    return self.name

  def getId(self):
    return self.id

  def draw(self, ctx, coords):  # reference: https://pycairo.readthedocs.io/  
    x = coords[0]["xViewPort"]
    y = coords[0]["yViewPort"]

    x2 = coords[1]["xViewPort"]
    y2 = coords[1]["yViewPort"]

    ctx.move_to(x,y)
    ctx.line_to(x2,y2)
    ctx.stroke()

  def drawToViewport(self, ctx, viewport):
    x, y = self.world_coords[0]["x"], self.world_coords[0]["y"]
    x2, y2 = self.world_coords[1]["x"], self.world_coords[1]["y"]

    point1 = viewport.transform(x, y)
    point2 = viewport.transform(x2, y2)

    ctx.move_to(point1["x"],point1["y"])
    ctx.line_to(point2["x"], point2["y"])
    ctx.stroke()

  def normalizeCoords(self, normalized_matrix):
    self.normalized_coords = []
    for i in self.world_coords:
      tmp = np.array([i["x"], i["y"], 1])
      tmp2 = tmp.dot(normalized_matrix)
      self.normalized_coords.append({"x": tmp2[0], "y": tmp2[1]})
    print(self.world_coords)
    print(self.normalized_coords)


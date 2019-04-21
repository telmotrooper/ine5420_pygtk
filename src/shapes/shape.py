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

  def drawToViewport(self, ctx, viewport):
    # move context to initial point
    point = viewport.transform(self.normalized_coords[0]["x"], self.normalized_coords[0]["y"])
    ctx.move_to(point["x"],point["y"])

    if(self.__class__.__name__ == "Point"):
      ctx.rel_line_to(1,1)  # equivalent to ctx.line_to(x+1,y+1)
      ctx.stroke()
    else:
      for entry in self.normalized_coords:  # 1st interation does move_to and line_to to same point
        x2, y2 = entry["x"], entry["y"]
        point2 = viewport.transform(x2, y2)
        ctx.line_to(point2["x"],point2["y"])
      ctx.close_path()
      ctx.stroke()
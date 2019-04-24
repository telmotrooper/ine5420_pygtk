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
    center = self.transform.denormalize(0,0)  # get world coordenates for current viewport center

    # get real world coordinates from normalized ones
    coords = self.transform.denormalizeList(self.normalized_coords)

    for i in range(len(coords)):
      temp = self.transform.scale(
        coords[i]["x"], coords[i]["y"],
        percentage, percentage,
        center["x"], center["y"]
      )
      new_coords = self.transform.normalize(temp[0], temp[1])
      self.normalized_coords[i] = {"x": new_coords["x"], "y": new_coords["y"]}
  
  def rotateNormalizedCoords(self, degrees):
    center = self.transform.denormalize(0,0)  # get world coordenates for current viewport center

    # get real world coordinates from normalized ones
    coords = self.transform.denormalizeList(self.normalized_coords)
    
    for i in range(len(coords)):
      temp = self.transform.rotation(coords[i]["x"], coords[i]["y"], center["x"], center["y"], degrees)
      new_coords = self.transform.normalize(temp[0], temp[1])
      self.normalized_coords[i] = {"x": new_coords["x"], "y": new_coords["y"]}

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
      # print("{},{}".format(self.normalized_coords[0]["x"], self.normalized_coords[0]["y"]))

      if (self.normalized_coords[0]["x"] >= -1 and self.normalized_coords[0]["x"] <= 1
          and self.normalized_coords[0]["y"] >= -1 and self.normalized_coords[0]["y"] <= 1):
        ctx.rel_line_to(1,1)  # equivalent to ctx.line_to(x+1,y+1)
        ctx.stroke()
    else:
      for entry in self.normalized_coords:  # 1st interation does move_to and line_to to same point
        x2, y2 = entry["x"], entry["y"]
        point2 = viewport.transform(x2, y2)
        ctx.line_to(point2["x"],point2["y"])
      ctx.close_path()
      ctx.stroke()

class Line:
  def __init__(self, name):
    self.world_coords = []
    self.normalized_coords = []
    self.name = name
  
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

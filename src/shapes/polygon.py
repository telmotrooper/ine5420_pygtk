class Polygon:
  coords = []

  def __init__(self, name):
    self.name = name
  
  def addCoords(self, x, y):
    self.coords.append(
      {"x": x, "y": y}
    )

  def draw(self, ctx):  # reference: https://pycairo.readthedocs.io/
    ctx.move_to(self.coords[0]["x"], self.coords[0]["y"])

    for entry in self.coords:  # 1st interation does move_to and line_to to same point
      x2 = entry["x"]
      y2 = entry["y"]
      ctx.line_to(x2,y2)

    ctx.stroke()

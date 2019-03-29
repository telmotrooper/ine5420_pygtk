class Line:
  coords = []

  def __init__(self, name):
    self.name = name
  
  def addCoords(self, x, y):
    self.coords.append(
      {"x": x, "y": y}
    )

  def draw(self, ctx):  # reference: https://pycairo.readthedocs.io/  
    x = self.coords[0]["x"]
    y = self.coords[0]["y"]

    x2 = self.coords[1]["x"]
    y2 = self.coords[1]["y"]

    ctx.move_to(x,y)
    ctx.line_to(x2,y2)
    ctx.stroke()

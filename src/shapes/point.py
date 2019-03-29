class Point:
  coords = []

  def __init__(self, name):
    self.name = name
  
  def addCoords(self, x, y):
    self.coords.append(
      {"x": x, "y": y}
    )

  def draw(self, ctx):
    x = self.coords[0]["x"]
    y = self.coords[0]["y"]

    ctx.move_to(x,y)
    ctx.rel_line_to(x+1,y+1)
    ctx.stroke()

class Point:
  def __init__(self, name):
    self.coords = []
    self.name = name
  
  def addCoords(self, x, y):
    self.coords.append(
      {"x": x, "y": y}
    )

  def getName(self):
    return self.name

  def draw(self, ctx):  # Reference: https://pycairo.readthedocs.io/    
    x = self.coords[0]["x"]
    y = self.coords[0]["y"]
  
    ctx.move_to(x,y)
    ctx.rel_line_to(1,1)  # equivalent to ctx.line_to(x+1,y+1)
    ctx.stroke()

import numpy as np
# pylint: disable=no-name-in-module, import-error
from utils.gen_random_id import generateRandomId
from transform import Transform
from shapes.shape import Shape

class Point(Shape):
  def __init__(self, name):
    super().__init__(name)

  def drawToViewport(self, ctx, viewport):   
    x, y = self.normalized_coords[0]["x"], self.normalized_coords[0]["y"]

    point = viewport.transform(x, y)
  
    ctx.move_to(point["x"],point["y"])
    ctx.rel_line_to(1,1)  # equivalent to ctx.line_to(x+1,y+1)
    ctx.stroke()

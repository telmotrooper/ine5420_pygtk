import numpy as np
# pylint: disable=no-name-in-module, import-error
from utils.gen_random_id import generateRandomId
from transform import Transform
from shapes.shape import Shape

class Line(Shape):
  def __init__(self, name):
    super().__init__(name)

  def drawToViewport(self, ctx, viewport):
    x, y = self.normalized_coords[0]["x"], self.normalized_coords[0]["y"]
    x2, y2 = self.normalized_coords[1]["x"], self.normalized_coords[1]["y"]

    point1 = viewport.transform(x, y)
    point2 = viewport.transform(x2, y2)

    ctx.move_to(point1["x"],point1["y"])
    ctx.line_to(point2["x"], point2["y"])
    ctx.stroke()

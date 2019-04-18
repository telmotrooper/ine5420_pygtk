import numpy as np
# pylint: disable=no-name-in-module, import-error
from utils.gen_random_id import generateRandomId
from transform import Transform
from shapes.shape import Shape

class Polygon(Shape):
  def __init__(self, name):
    super().__init__(name)

  def drawToViewport(self, ctx, viewport):
    # move context to initial point
    point = viewport.transform(self.normalized_coords[0]["x"], self.normalized_coords[0]["y"])
    ctx.move_to(point["x"],point["y"])

    for entry in self.normalized_coords:  # 1st interation does move_to and line_to to same point
      x2, y2 = entry["x"], entry["y"]
      point2 = viewport.transform(x2, y2)
      ctx.line_to(point2["x"],point2["y"])
    ctx.close_path()
    ctx.stroke()

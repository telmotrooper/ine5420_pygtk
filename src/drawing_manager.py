from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon

class DrawingManager:
  def draw_background(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255)  # color white
    ctx.paint()

  def draw(self, da, ctx):
    self.draw_background(da, ctx)

    ctx.set_source_rgb(0, 0, 0)  # color black
    ctx.set_line_width(2)

    l = Line("Line 1")
    l.addCoords(100, 50)
    l.addCoords(146, 200)
    l.draw(ctx)

    p = Point("Point 1")
    p.addCoords(20, 200)  
    p.draw(ctx)

    po = Polygon("Polygon 1")
    po.addCoords(300, 300)
    po.addCoords(400, 200)
    po.addCoords(250, 50)
    po.draw(ctx)

    po2 = Polygon("Polygon 2")  # fix this: when adding a 2nd polygon it bugs the 1st one
    po2.addCoords(500, 500)
    # po2.addCoords(220, 300)
    # po2.addCoords(250, 100)
    # po2.addCoords(700, 50)
    po2.draw(ctx)

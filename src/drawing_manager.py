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

    l1 = Line("Line 1")
    l1.addCoords(100, 50)
    l1.addCoords(146, 200)
    l1.draw(ctx)

    l2 = Line("Line 2")
    l2.addCoords(150, 60)
    l2.addCoords(180, 60)
    l2.draw(ctx)

    p1 = Point("Point 1")
    p1.addCoords(20, 200)  
    p1.draw(ctx)

    po1 = Polygon("Polygon 1")
    po1.addCoords(300, 300)
    po1.addCoords(400, 200)
    po1.addCoords(250, 50)
    po1.draw(ctx)

    po2 = Polygon("Polygon 2")  # fix this: when adding a 2nd polygon it bugs the 1st one
    po2.addCoords(500, 500)
    po2.addCoords(320, 400)
    po2.addCoords(450, 300)
    po2.addCoords(800, 250)
    po2.draw(ctx)

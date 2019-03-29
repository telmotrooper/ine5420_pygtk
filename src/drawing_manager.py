from shapes.point import Point
from shapes.line import Line

class DrawingManager:
  def draw_background(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255)  # color white
    ctx.paint()

  def draw(self, da, ctx):
    self.draw_background(da, ctx)

    ctx.set_source_rgb(0, 0, 0)  # color black
    ctx.set_line_width(2)

    l = Line("Line 1")
    l.addCoords(100,50)
    l.addCoords(146,200)
    l.draw(ctx)

    p = Point("Point 1")
    p.addCoords(20, 200)  
    p.draw(ctx)

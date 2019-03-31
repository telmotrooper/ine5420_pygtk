from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon

class DrawingManager:
  def draw_background(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255)  # color white
    ctx.paint()

  def draw(self, da, ctx):
    self.draw_background(da, ctx)
    self.da = da
    self.ctx = ctx

  def reDraw(self, displayfile):
    for i in displayfile.getObjects():
      i.draw(self.ctx)

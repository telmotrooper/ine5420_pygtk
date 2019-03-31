from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from display_file import DisplayFile
from viewport import Viewport

class DrawingManager:
  def __init__(self):
    self.display_file = DisplayFile()
    self.draw_counter = 0
    self.viewport = Viewport()

  def draw_background(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255)  # color white
    ctx.paint()

  def draw(self, da, ctx):
    self.draw_background(da, ctx)

    ctx.set_source_rgb(0, 0, 0)  # color black
    ctx.set_line_width(2)
    if self.display_file.getObjects():
      '''for i in self.display_file.getObjects():
        print('Drawing object "{}"'.format(i.getName()))
        i.draw(ctx)

      self.draw_counter += 1
      print("draw() #{0}".format(self.draw_counter))'''
      self.viewport.transformada(ctx)

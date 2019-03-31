from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from display_file import DisplayFile

class DrawingManager:
  def __init__(self):
    self.display_file = DisplayFile()

  def draw_background(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255)  # color white
    ctx.paint()

  def draw(self, da, ctx):
    print("I'M DRAWING")
    self.draw_background(da, ctx)

    ctx.set_source_rgb(0, 0, 0)  # color black
    ctx.set_line_width(2)
    
    for i in self.display_file.getObjects():
      print("DRAW OBJECT")
      i.draw(ctx)

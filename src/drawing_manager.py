from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from display_file import DisplayFile
from window import Window
from viewport import Viewport

class DrawingManager:
  def __init__(self):
    self.display_file = DisplayFile()
    self.draw_counter = 0
    self.window = Window(0, 0, 1000, 1000)  # 1000x1000 is a placeholder for the real value
    self.viewport = Viewport(0, 0, 1000, 1000)

  def draw_background(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255)  # color white
    ctx.paint()

  def draw(self, da, ctx):
    da_width = da.get_allocation().width
    da_height = da.get_allocation().height

    self.window.setMax(da_width, da_height)  # This will cause problems with zoom

    self.viewport.setWindow(self.window)
    self.viewport.setMax(da_width, da_height)

    self.draw_background(da, ctx)

    ctx.set_source_rgb(0, 0, 0)  # color black
    ctx.set_line_width(2)
    
    for i in self.display_file.getObjects():
      print('Drawing object "{}"'.format(i.getName()))
      i.drawToViewport(ctx, self.viewport)

    self.draw_counter += 1
    print("draw() #{0}".format(self.draw_counter))

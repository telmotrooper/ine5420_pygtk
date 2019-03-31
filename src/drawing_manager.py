from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from display_file import DisplayFile
from window import Window
from viewport import Viewport

class DrawingManager:
  def __init__(self, da):
    self.display_file = DisplayFile()
    self.draw_counter = 0
    self.da = da

    da_width = da.get_allocation().width
    da_height = da.get_allocation().height

    # Window and viewport start with the same size as the drawing area
    self.window = Window(0, 0, da_width, da_height)
    self.viewport = Viewport(0, 0, da_width, da_height)

    self.viewport.setWindow(self.window)

  def getWindow(self):
    return self.window

  def drawBackground(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255)  # color white
    ctx.paint()

  def draw(self, da, ctx):
    self.drawBackground(da, ctx)

    ctx.set_source_rgb(0, 0, 0)  # color black
    ctx.set_line_width(2)
    
    for i in self.display_file.getObjects():
      print('Drawing object "{}"'.format(i.getName()))
      i.drawToViewport(ctx, self.viewport)

    self.draw_counter += 1
    print("draw() #{0}".format(self.draw_counter))

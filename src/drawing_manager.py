from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from display_file import DisplayFile
from window import Window
from transform import Transform
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

    self.transform = Transform()

    # Pass reference to window for Transform and Viewport
    self.transform.setWindow(self.window)
    self.viewport.setWindow(self.window)

    # To verify that both normalize() and denormalize() work
    # print(self.transform.normalize(0,0))
    # print(self.transform.normalize(self.window.getWidth(),self.window.getHeight()))
    # print(self.transform.denormalize(-1,-1))
    # print(self.transform.denormalize(1,1))


  def getWindow(self):
    return self.window

  def redraw(self):
    self.da.queue_draw()

  def drawBackground(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255)  # color white
    ctx.paint()

  def draw(self, da, ctx):
    self.drawBackground(da, ctx)

    ctx.set_source_rgb(0, 0, 0)  # color black
    ctx.set_line_width(2)
    
    for i in self.display_file.getObjects():
      # print('Drawing object "{}"'.format(i.getName()))
      i.drawToViewport(ctx, self.viewport)

      self.draw_counter += 1
      print("draw() #{0}".format(self.draw_counter))

from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from shapes.point3d import Point3D
from shapes.object3d import Object3D
from display_file import DisplayFile
from window import Window
from transform import Transform
from viewport import Viewport
from variables import clipping_border_size as cbz
from clipping import Clipping
import copy

class DrawingManager:
  def __init__(self, da):
    self.display_file = DisplayFile()
    self.draw_counter = 0
    self.da = da

    da_width = da.get_allocation().width
    da_height = da.get_allocation().height

    # Window and viewport start with the same size as the drawing area,
    # but compensating for the clipping border size (otherwise you 
    # wouldn't see by default a point drawn at 0,0).
    self.window = Window(-cbz, -cbz, da_width - cbz, da_height - cbz)
    self.viewport = Viewport(-cbz, -cbz, da_width - cbz, da_height - cbz)

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

  def drawClippingBorder(self, da, ctx):
    ctx.set_line_width(1)
    ctx.set_source_rgb(255, 0, 0) # color red

    ctx.move_to(cbz, cbz)
    ctx.line_to(self.window.getWidth() - cbz, cbz)
    ctx.line_to(self.window.getWidth() - cbz, self.window.getHeight() - cbz)
    ctx.line_to(cbz, self.window.getHeight() - cbz)

    ctx.close_path()
    ctx.stroke()

  def draw(self, da, ctx):
    self.drawBackground(da, ctx)

    ctx.set_line_width(2)
    ctx.set_source_rgb(0, 0, 0)  # color black
    
    for i in self.display_file.getObjects():
      # print('Drawing object "{}"'.format(i.getName()))
      i.drawToViewport(ctx, self.viewport)

      self.draw_counter += 1
      # print("draw() #{0}".format(self.draw_counter))
    
    for i in self.display_file.getObjects3d():
      obj_perspectiva = copy.deepcopy(i)
      lista_pontos_3d = []
      for segmento in obj_perspectiva.segments:
        lista_pontos_3d.append(segmento[0])
        lista_pontos_3d.append(segmento[1])

      self.transform.perspectiva(lista_pontos_3d, 100)

      for s in obj_perspectiva.segments:
          print(s[0].x, s[0].y)
          print(s[1].x, s[1].y)


          coords0 = self.viewport.transformadaViewPortCoordenada(s[0].x, s[0].y)
          coords1 = self.viewport.transformadaViewPortCoordenada(s[1].x, s[1].y)
          ctx.move_to(coords0['x'], coords0['y'])
          ctx.line_to(coords1['x'], coords1['y'])

      '''
      for s in i.segments:
        reta = [{"x": s[0].x, "y": s[0].y},{"x": s[1].x, "y": s[1].y}]
        clipping = Clipping()
        coords = clipping.cohenSutherland(reta, self.window)
        if(coords):
          coords0 = self.viewport.transformadaViewPortCoordenada(coords[0]['x'], coords[0]['y'])
          coords1 = self.viewport.transformadaViewPortCoordenada(coords[1]['x'], coords[1]['y'])
          ctx.move_to(coords0['x'], coords0['y'])
          ctx.line_to(coords1['x'], coords1['y'])
'''
    ctx.stroke()
    

    self.drawClippingBorder(da, ctx)


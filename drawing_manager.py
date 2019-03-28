from shapes.point import Point

class DrawingManager:
  def draw_background(self, da, ctx):
    ctx.set_source_rgb(255, 255, 255) # color white
    ctx.paint()

  def draw(self, da, ctx):
    self.draw_background(da, ctx)

    ctx.set_source_rgb(255, 255, 255) # color white
    ctx.paint()

    ctx.set_source_rgb(0, 0, 0) # color black
    
    ctx.set_line_width(2)
    ctx.move_to(20, 20)
    ctx.rel_line_to(50,50)
    ctx.stroke()

    p = Point("Point 1")
    p.addCoords(20, 200)  
    p.draw(ctx)

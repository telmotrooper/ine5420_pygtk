from transform import Transform
from display_file import DisplayFile
import numpy as np

class Window:
  orientation = 0
  current_zoom = 1

  def __init__(self, x_min, y_min, x_max, y_max):
    print("({},{}) ({},{})".format(x_min, y_min, x_max, y_max))

    Window.x_min = x_min
    Window.y_min = y_min
    Window.x_max = x_max
    Window.y_max = y_max
    Window.transform = Transform()
    Window.display_file = DisplayFile()

  def getMin(self):
    return { "x": Window.x_min, "y": Window.y_min }

  def getMax(self):
    return { "x": Window.x_max, "y": Window.y_max }

  def getWidth(self):
    return Window.x_max - Window.x_min
  
  def getHeight(self):
    return Window.y_max - Window.y_min

  def getCenter(self):
    # print("window from ({},{}) to ({},{})".format(Window.x_min, Window.y_min, Window.x_max, Window.y_max))
    width, height = self.getWidth(), self.getHeight()

    center_x = (width / 2) + Window.x_min
    center_y = (height / 2) + Window.y_min

    # print("center at ({},{})".format(center_x, center_y))
    
    return {
      "x": center_x,
      "y": center_y
    }

  def zoom(self, percentage, caller=None):
    temp = percentage

    if(caller == None):
      self.current_zoom *= percentage
    elif(caller == "move"):
      temp = self.current_zoom

    for i in self.display_file.getObjects():
      i.scaleNormalizedCoords(temp)

  def setMin(self, x, y):
    Window.x_min = x
    Window.y_min = y
  
  def setMax(self, x, y):
    Window.x_max = x
    Window.y_max = y

  def move(self, x, y):
    Window.x_min += x
    Window.y_min += y
    Window.x_max += x
    Window.y_max += y

    for i in Window.display_file.getObjects():
      i.normalizeCoords()

    self.rotate(0)
    # self.zoom(self.current_zoom, "move")

  def rotate(self, angle):    
    # sum rotation angle, since objects don't hold state for their rotations
    self.orientation += angle

    for i in self.display_file.getObjects():
      i.rotateNormalizedCoords(self.orientation,)

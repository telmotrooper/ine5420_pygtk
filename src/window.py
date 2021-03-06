from transform import Transform
from display_file import DisplayFile
import numpy as np

class Window:
  def __init__(self, x_min, y_min, x_max, y_max):
    #print("({},{}) ({},{})".format(x_min, y_min, x_max, y_max))

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
    for i in self.display_file.getObjects():
      i.scaleNormalizedCoords(percentage)
    
    for j in self.display_file.getObjects3d():
      j.scale(percentage)


  def setMin(self, x, y):
    Window.x_min = x
    Window.y_min = y
  
  def setMax(self, x, y):
    Window.x_max = x
    Window.y_max = y

  def move(self, x, y):
    obj_coords = []

    # get normalized coordenates for all objects and denormalize them
    for i in Window.display_file.getObjects():
      norm_coords = i.getNormalizedCoords()
      obj_coords.append(self.transform.denormalizeList(norm_coords))

    Window.x_min += x
    Window.y_min += y
    Window.x_max += x
    Window.y_max += y

    objects = Window.display_file.getObjects()

    # renormalize all coords after the window has been resized
    for i in range(len(objects)):
      objects[i].normalized_coords = self.transform.normalizeList(obj_coords[i])

    #print("({},{}) ({},{})".format(Window.x_min, Window.y_min, Window.x_max, Window.y_max))

  def rotate(self, angle):    
    for i in self.display_file.getObjects():
      i.rotateNormalizedCoords(angle)

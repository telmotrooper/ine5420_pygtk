from transform import Transform
from display_file import DisplayFile
import numpy as np

class Window:
  def __init__(self, x_min, y_min, x_max, y_max):
    Window.x_min = x_min
    Window.y_min = y_min
    Window.x_max = x_max
    Window.y_max = y_max
    Window.transformation = Transform()
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
    width, height = self.getWidth(), self.getHeight()
    return {
      "x": width / 2,
      "y": height / 2
    }

  def zoom(self, percentage):
    new_height = self.getHeight() / percentage
    new_width =  self.getWidth() / percentage
    
    new_x_min = (self.getCenter()["x"] - new_width) / 2
    new_y_min = (self.getCenter()["y"] - new_height) / 2
    self.setMin(new_x_min, new_y_min)

    new_x_max = (self.getCenter()["x"] + new_width) / 2
    new_y_max = (self.getCenter()["y"] + new_height) / 2
    self.setMax(new_x_max, new_y_max)

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

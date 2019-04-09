from transform import Transform
from display_file import DisplayFile
import numpy as np

class Window:
  def __init__(self, x_min, y_min, x_max, y_max):
    self.x_min, self.normalized_x_min = x_min, x_min
    self.y_min, self.normalized_y_min = y_min, y_min
    self.x_max, self.normalized_x_max = x_max, x_max
    self.y_max, self.normalized_y_max = y_max, y_max
    self.transformation = Transform()
    self.display_file = DisplayFile()

  def getMin(self):
    return { "x": self.x_min, "y": self.y_min }

  def getMax(self):
    return { "x": self.x_max, "y": self.y_max }

  def getNormalizedMin(self):
    return { "x": self.x_min, "y": self.y_min }

  def getNormalizedMax(self):
    return { "x": self.x_max, "y": self.y_max }

  def getWidth(self):
    return self.x_max - self.x_min
  
  def getHeight(self):
    return self.y_max - self.y_min

  def getNormalizedWidth(self):
    return self.normalized_x_max - self.normalized_x_min
  
  def getNormalizedHeight(self):
    return self.normalized_y_max - self.normalized_y_min
  
  def getCenter(self):
    width, height = self.getWidth(), self.getHeight()
    return {
      "x": width / 2,
      "y": height / 2
    }

  def normalize(self):
    translated = self.transformation.normalize_translation(-self.getCenter()["x"],-self.getCenter()["y"])
    rotated = self.transformation.normalize_rotation(30)
    scaled = self.transformation.normalize_scale(2/self.getWidth(), 2/self.getHeight())
    tmp1 = translated.dot(rotated).dot(scaled)
    for i in self.display_file.getObjects():
      i.normalizeCoords(tmp1)

  

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
    self.x_min = x
    self.y_min = y
  
  def setMax(self, x, y):
    self.x_max = x
    self.y_max = y

  def move(self, x, y):
    self.x_min += x
    self.y_min += y
    self.x_max += x
    self.y_max += y

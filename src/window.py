class Window:
  def __init__(self, x_min, y_min, x_max, y_max):
    self.x_min = x_min
    self.y_min = y_min
    self.x_max = x_max
    self.y_max = y_max

  def getMin(self):
    return { "x": self.x_min, "y": self.y_min }

  def getMax(self):
    return { "x": self.x_max, "y": self.y_max }

  def getWidth(self):
    return self.x_max - self.x_min
  
  def getHeight(self):
    return self.y_max - self.y_min
  
  def getCenter(self):
    return {
      "x": self.getWidth() / 2,
      "y": self.getHeight() / 2
    }

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

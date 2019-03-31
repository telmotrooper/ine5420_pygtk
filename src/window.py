class Window:
  beginning_coords = {"x": 0, "y": 0}
  ending_coords = {"x": 300, "y": 300}
  
  def addBeginningCoords(self, x, y):
    self.beginning_coords = {"x": x, "y": y}

  def addEndingCoords(self, x, y):
    self.ending_coords = {"x": x, "y": y}

  def getBeginningWindow(self):
    return self.beginning_coords

  def getEndingWindow(self):
    return self.ending_coords

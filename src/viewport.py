from window import Window

class Viewport(Window):
  def __init__(self, x_min, y_min, x_max, y_max):
    super().__init__(x_min, y_min, x_max, y_max)
  
  def setWindow(self, window):
    self.xw_min = window.getMin()["x"]
    self.yw_min = window.getMin()["y"]
    self.xw_max = window.getMax()["x"]
    self.yw_max = window.getMax()["y"]

  def transform(self, x, y):
    xw_min, yw_min = self.xw_min, self.yw_min
    xw_max, yw_max = self.xw_max, self.yw_max

    xvp_min, yvp_min = self.x_min, self.y_min
    xvp_max, yvp_max = self.x_max, self.y_max

    xvp = ((x - xw_min)/(xw_max - xw_min)) * (xvp_max - xvp_min)
    yvp = (1 - (y - yw_min)/(yw_max - yw_min)) * (yvp_max - yvp_min)
    return { "x": xvp, "y": yvp }

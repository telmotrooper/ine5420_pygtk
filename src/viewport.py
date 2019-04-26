from window import Window
from transform import Transform

class Viewport(Window):
  def __init__(self, x_min, y_min, x_max, y_max):
    super().__init__(x_min, y_min, x_max, y_max)
    self.t = Transform()
  
  def setWindow(self, window):
    self.window = window

  def transform(self, x, y):
    xw_min, yw_min = self.window.getMin()["x"], self.window.getMin()["y"]
    xw_max, yw_max = self.window.getMax()["x"], self.window.getMax()["y"]

    xvp_min, yvp_min = self.x_min, self.y_min
    xvp_max, yvp_max = self.x_max, self.y_max

    denormalized_point = self.t.denormalize(x, y)

    xvp = ((denormalized_point["x"] - xw_min)/(xw_max - xw_min)) * (xvp_max - xvp_min)
    yvp = (1 - (denormalized_point["y"] - yw_min)/(yw_max - yw_min)) * (yvp_max - yvp_min)
    print(xvp, yvp)
    return { "x": xvp, "y": yvp }

from window import Window

class Viewport(Window):
  def __init__(self, x_min, y_min, x_max, y_max):
    super().__init__(x_min, y_min, x_max, y_max)
  
  def transform(self, window, x, y):
    xw_min = window.getMin()["x"]
    yw_min = window.getMin()["y"]
    xw_max = window.getMax()["x"]
    yw_max = window.getMax()["y"]

    xvp_min = self.x_min
    yvp_min = self.y_min
    xvp_max = self.x_max
    yvp_max = self.y_max

    xvp = ((x - xw_min)/(xw_max - xw_min)) * (xvp_max - xvp_min)
    yvp = (1 - (y - yw_min)/(yw_max - yw_min)) * (yvp_max - yvp_min)
    return { "x": xvp, "y": yvp }

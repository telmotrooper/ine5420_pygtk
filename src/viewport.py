from display_file import DisplayFile
from window import Window

class Viewport:
  def __init__(self):
    self.beginning_coords = {"x": 0, "y": 0}
    self.ending_coords = {"x": 300, "y": 300}
  
  def transformada(self, ctx):
    displayFile = DisplayFile()
    window = Window()
    for obj in displayFile.getObjects():
      coordsInVp = []
      coordsObj = obj.getCoords()
      for coords in coordsObj:
        print(window.getBeginningWindow())
        coordsInVp.append(self.calculoTransformada(coords, window.getBeginningWindow(), window.getEndingWindow()))
      obj.draw(ctx, coordsInVp)

  def calculoTransformada(self, coords, window_beginning, window_ending):
    xViewport = ((coords["x"] - window_beginning["x"])/(window_ending["x"] - window_beginning["x"])) * (self.ending_coords["x"] - self.beginning_coords["x"])
    yViewport = (1 - (coords["y"] - window_beginning["y"])/(window_ending["y"] - window_beginning["y"])) * (self.ending_coords["y"] - self.beginning_coords["y"])
    return { "xViewPort": xViewport, "yViewPort": yViewport }

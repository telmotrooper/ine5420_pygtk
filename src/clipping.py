import numpy as np
import operator
from functools import reduce
import copy

class Clipping:
  def __init__(self):
    self.INSIDE = 0
    self.LEFT = 1
    self.RIGHT = 2
    self.BOTTOM = 4
    self.TOP = 8

  def region_code(self, x, y):
    xw_min, xw_max = -1, 1
    yw_min, yw_max = -1, 1
    code = self.INSIDE
    if x < xw_min:
      code |= self.LEFT
    if x > xw_max:
      code |= self.RIGHT
    if y < yw_min:
      code |= self.BOTTOM
    if y > yw_max:
      code |= self.TOP
    
    return code
  

  def cohenSutherland(self, copy_coords):
    copy_coords = copy.deepcopy(copy_coords)
    xw_min, xw_max = -1, 1
    yw_min, yw_max = -1, 1

    code_0 = self.region_code(copy_coords[0]["x"], copy_coords[0]["y"])
    code_1 = self.region_code(copy_coords[1]["x"], copy_coords[1]["y"])

    aceita = False

    while True:
      if not(code_0 | code_1):
        aceita = True
        break
      
      if code_0 & code_1:
        break
      
      else:
        x = 0
        y = 0
        _code = None

        if code_0:
          _code = code_0
        else:
          _code = code_1
        
        if _code & self.TOP:
          x = copy_coords[0]["x"] + (copy_coords[1]["x"] - copy_coords[0]["x"]) * (yw_max - copy_coords[0]["y"]) / (copy_coords[1]["y"] - copy_coords[0]["y"])
          y = yw_max
        
        if _code & self.BOTTOM:
          x = copy_coords[0]["x"] + (copy_coords[1]["x"] - copy_coords[0]["x"]) * (yw_min - copy_coords[0]["y"]) / (copy_coords[1]["y"] - copy_coords[0]["y"])
          y = yw_min
        
        if _code & self.RIGHT:
          y = copy_coords[0]["y"] + (copy_coords[1]["y"] - copy_coords[0]["y"]) * (xw_max - copy_coords[0]["x"]) / (copy_coords[1]["x"] - copy_coords[0]["x"])
          x = xw_max
        
        if _code & self.LEFT:
          y = copy_coords[0]["y"] + (copy_coords[1]["y"] - copy_coords[0]["y"]) * (xw_min - copy_coords[0]["x"]) / (copy_coords[1]["x"] - copy_coords[0]["x"])
          x = xw_min
        
        if _code == code_0:
          copy_coords[0]["x"] = x
          copy_coords[0]["y"] = y

          code_0 = self.region_code(copy_coords[0]["x"], copy_coords[0]["y"])
        
        else:
          copy_coords[1]["x"] = x
          copy_coords[1]["y"] = y

          code_1 = self.region_code(copy_coords[1]["x"], copy_coords[1]["y"])
    
    return copy_coords
      


  

  def liangBarsky(self, copy_coords):
    copy_coords = copy.deepcopy(copy_coords)
    xw_min, xw_max = -1, 1
    yw_min, yw_max = -1, 1

    u1 = 0.0
    u2 = 1.0
    dx = copy_coords[1]["x"] - copy_coords[0]["x"]
    dy = copy_coords[1]["y"] - copy_coords[0]["y"]
    p = 0.0
    q = 0.0
    r = 0.0
    draw = True

    edge = 0
    while edge < 4:
      if edge == 0:
          p = -dx
          q = copy_coords[0]["x"] - xw_min

      if edge == 1:
          p = dx
          q = xw_max - copy_coords[0]["x"]

      if edge == 2:
          p = -dy
          q = copy_coords[0]["y"] - yw_min

      if edge == 3:
          p = dy
          q = yw_max - copy_coords[0]["y"]

      if p == 0:
          p = 1

      r = q / p

      if p == 0 and q < 0:
          draw = False

      if p < 0:
          if r > u2:
              draw = False
          if r > u1:
              u1 = r

      if p > 0:
          if r < u1:
              draw = False
          if r < u2:
              u2 = r
      edge += 1

    if draw:
      copy_coords[0]["x"] = copy_coords[0]["x"] + u1 * dx
      copy_coords[0]["y"] = copy_coords[0]["y"] + u1 * dy
      copy_coords[1]["x"] = copy_coords[0]["x"] + u2 * dx
      copy_coords[1]["y"] = copy_coords[0]["y"] + u2 * dy

    return copy_coords

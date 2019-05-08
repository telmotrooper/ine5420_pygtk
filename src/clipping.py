import numpy as np
import operator
from functools import reduce
import copy

class Clipping:
  def regionCode(self, x, y):
    xw_min, xw_max = -1, 1
    yw_min, yw_max = -1, 1
    rc = np.array([0,0,0,0])
    rc[3] = 1 if (x < xw_min) else 0 
    rc[2] = 1 if (x > xw_max) else 0
    rc[1] = 1 if (y < yw_min) else 0
    rc[0] = 1 if (y > yw_max) else 0

    return rc
  
  def visibility(self, initial, final):
    initial_all_zeros = np.all(initial==0)
    final_all_zeros = np.all(final==0)
    equal = (initial==final).all()
    logical = reduce(operator.and_, [initial, final])
    
    if(initial_all_zeros and final_all_zeros and equal):
      return 'inside'
    if(not np.all(logical==0)):
      return 'out'
    if(np.all(logical==0) and not equal):
      return 'partial'

  def coef_angular(self, normalized_coords):
    return (normalized_coords[1]["y"] - normalized_coords[0]["y"])/(normalized_coords[1]["x"] - normalized_coords[0]["x"])

  def cohenSutherland(self, copy_coords):
    copy_coords = copy.deepcopy(copy_coords)

    initial = self.regionCode(copy_coords[0]["x"], copy_coords[0]["y"])
    final = self.regionCode(copy_coords[1]["x"], copy_coords[1]["y"])
    visibility = self.visibility(initial, final)
    print(initial)
    print(final)
    if(visibility == 'partial'):
      m = self.coef_angular(copy_coords)

      if(np.array_equal(initial, [0, 0, 0, 1])): # a esquerda
        y = m * (-1 - copy_coords[0]["x"]) + copy_coords[0]["y"]
        if(y > -1 and y < 1):
          copy_coords[0]["x"] = -1
          copy_coords[0]["y"] = y
      
      if(np.array_equal(final, [0, 0, 1, 0])): # a direita
        y = m * (1 - copy_coords[0]["x"]) + copy_coords[0]["y"]
        if(y > -1 and y < 1):
          copy_coords[1]["x"] = 1
          copy_coords[1]["y"] = y
      
      if(np.array_equal(final, [1, 0, 0, 0])): # topo
        x = copy_coords[0]["x"] + 1/m * (1 - copy_coords[0]["y"])
        if(x > -1 and x < 1):
          copy_coords[1]["x"] = x
          copy_coords[1]["y"] = 1

      if(np.array_equal(initial, [0, 1, 0, 0])): # embaixo
        x = copy_coords[0]["x"] + 1/m * (-1 - copy_coords[0]["y"])
        if(x > -1 and x < 1):
          copy_coords[0]["x"] = x
          copy_coords[0]["y"] = -1
      
      if(np.array_equal(initial, [0, 1, 0, 1])): # esquerda embaixo
        y = m * (-1 - copy_coords[0]["x"]) + copy_coords[0]["y"]
        if(y > -1 and y < 1):
          copy_coords[0]["x"] = -1
          copy_coords[0]["y"] = y
        
        x = copy_coords[0]["x"] + 1/m * (-1 - copy_coords[0]["y"])
        if(x > -1 and x < 1):
          copy_coords[0]["x"] = x
          copy_coords[0]["y"] = -1

      if(np.array_equal(initial, [1, 0, 0, 1])): # a esquerda
        y = m * (-1 - copy_coords[0]["x"]) + copy_coords[0]["y"]
        if(y > -1 and y < 1):
          copy_coords[0]["x"] = -1
          copy_coords[0]["y"] = y
        
        x = copy_coords[0]["x"] + 1/m * (1 - copy_coords[0]["y"])
        if(x > -1 and x < 1):
          copy_coords[1]["x"] = x
          copy_coords[1]["y"] = 1
      
      if(np.array_equal(final, [0, 0, 1, 0])): # a direita topo
        y = m * (1 - copy_coords[0]["x"]) + copy_coords[0]["y"]
        if(y > -1 and y < 1):
          copy_coords[1]["x"] = 1
          copy_coords[1]["y"] = y
        
        x = copy_coords[0]["x"] + 1/m * (1 - copy_coords[0]["y"])
        if(x > -1 and x < 1):
          copy_coords[1]["x"] = x
          copy_coords[1]["y"] = 1
      
      if(np.array_equal(final, [0, 0, 1, 0])): # a direita embaixo
        y = m * (1 - copy_coords[0]["x"]) + copy_coords[0]["y"]
        if(y > -1 and y < 1):
          copy_coords[1]["x"] = 1
          copy_coords[1]["y"] = y
        
        x = copy_coords[0]["x"] + 1/m * (-1 - copy_coords[0]["y"])
        if(x > -1 and x < 1):
          copy_coords[0]["x"] = x
          copy_coords[0]["y"] = -1
          
    return copy_coords
      
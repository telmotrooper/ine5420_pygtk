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
      
  def liangBarsky(self, copy_coords):
    
    copy_coords = copy.deepcopy(copy_coords)
    p1 = -(copy_coords[1]["x"] - copy_coords[0]["x"]) 
    p2 = (copy_coords[1]["x"] - copy_coords[0]["x"]) 
    p3 = -(copy_coords[1]["y"] - copy_coords[0]["y"]) 
    p4 = (copy_coords[1]["y"] - copy_coords[0]["y"]) 
    q1 = copy_coords[0]["x"] - (-1)
    q2 = 1 - copy_coords[0]["x"]
    q3 = copy_coords[0]["y"] - (-1)
    q4 = 1 - copy_coords[0]["y"]
    
    if(p1 < 0 and p3 < 0): #fora pra dentro
      r1 = q1/p1 # esquerda
      r3 = q3/p3 # baixo
      symbol1 = max(0, r1, r3)
      if(symbol1 > 0):
        copy_coords[0]["x"] = copy_coords[0]["x"] + symbol1 * p2
        copy_coords[0]["y"] = copy_coords[0]["y"] + symbol1 * p4
    
    if(p2 > 0 and p4 > 0): # dentro pra fora
      r2 = q2/p2 # direita
      r4 = q4/p4 # topo
      symbol2 = min(1, r2, r4)
      if(symbol2 < 1):
        copy_coords[1]["x"] = copy_coords[0]["x"] + symbol2 * p2
        copy_coords[1]["y"] = copy_coords[0]["y"] + symbol2 * p4
      
    p1 = -(copy_coords[0]["x"] - copy_coords[1]["x"])
    p2 = (copy_coords[0]["x"] - copy_coords[1]["x"])
    p3 = -(copy_coords[0]["y"] - copy_coords[1]["y"])
    p4 = (copy_coords[0]["y"] - copy_coords[1]["y"])
    q1 = copy_coords[1]["x"] - (-1)
    q2 = 1 - copy_coords[1]["x"]
    q3 = copy_coords[1]["y"] - (-1)
    q4 = 1 - copy_coords[1]["y"]
    
    if(p2 < 0 and p4 < 0):
      r2 = q2/p2
      r4 = q4/p4
      symbol1 = max(0, r2, r4)
      if(symbol1 > 0):
        copy_coords[1]["x"] = copy_coords[1]["x"] + symbol1 * p2
        copy_coords[1]["y"] = copy_coords[1]["y"] + symbol1 * p4
    
    if(p1 > 0 and p3 > 0):
      r1 = q1/p1
      r3 = q3/p3
      symbol2 = min(1, r1, r3)
      if(symbol2 < 1):
        copy_coords[0]["x"] = copy_coords[1]["x"] + symbol2 * p2
        copy_coords[0]["y"] = copy_coords[1]["y"] + symbol2 * p4
  
    return copy_coords

import numpy as np

class Matrices:
  def point(self, x, y):
    return np.array([x, y, 1])
  
  def translation(self, dx, dy):
    return np.array([[1,  0,  0],
                     [0,  1,  0],
                     [dx, dy, 1]])

  def scaling(self, sx, sy):
    return np.array([[sx,  0, 0],
                     [0 , sy, 0],
                     [0 ,  0, 1]])

  def rotation(self, degrees):
    sin = np.sin(np.deg2rad(degrees))
    cos = np.cos(np.deg2rad(degrees))

    return np.array([[cos, -sin, 0],
                     [sin,  cos, 0],
                     [ 0 ,   0 , 1]])

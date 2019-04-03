import numpy as np

def translation(x, y, dx, dy):
  a = np.array([x, y, 1])
  b = np.array([[1,0,0], [0,1,0], [dx, dy, 1]])
  return a.dot(b)

def escale(x, y, sx, sy):
  a = np.array([x, y, 1])
  b = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
  return a.dot(b)

def rotation(x, y, degrees):
  sin = np.sin(np.deg2rad(degrees))
  cos = np.cos(np.deg2rad(degrees))
  a = np.array([x, y, 1])
  b = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
  return a.dot(b)

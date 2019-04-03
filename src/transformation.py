import numpy as np
from display_file import DisplayFile

display_file = DisplayFile()

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

def move(tree_view, x, y):
  obj_list, index = tree_view.get_selection().get_selected()
  obj_name = obj_list[index][0]
  obj = display_file.getObject(obj_name)
  coords = obj.getCoords()

  for i in range(len(coords)):
    new_coords = translation(coords[i]["x"], coords[i]["y"], x, y)
    coords[i] = {"x": new_coords[0], "y": new_coords[1]}
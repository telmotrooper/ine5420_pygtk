import numpy as np
from display_file import DisplayFile

display_file = DisplayFile()

def translation(x, y, dx, dy):
  a = np.array([x, y, 1])
  b = np.array([[1,0,0], [0,1,0], [dx, dy, 1]])
  return a.dot(b)

def scale(x, y, sx, sy, cx, cy):
  a = np.array([x, y, 1])
  b = np.array([[1,0,0],[0,1,0],[-cx, -cy, 1]])
  c = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
  d = np.array([[1,0,0],[0,1,0],[cx, cy, 1]])
  
  return a.dot(b).dot(c).dot(d)

def rotation(x, y, degrees):
  sin = np.sin(np.deg2rad(degrees))
  cos = np.cos(np.deg2rad(degrees))
  a = np.array([x, y, 1])
  b = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
  return a.dot(b)

def center(coords):
  x = 0
  y = 0
  count = 0
  for i in coords:
    x += i["x"]
    y += i["y"]
    count += 1
  
  return {"cx": x/count, "cy": y/count}

def move(tree_view, x, y):
  obj_list, index = tree_view.get_selection().get_selected()
  obj_name = obj_list[index][0]
  obj = display_file.getObject(obj_name)
  coords = obj.getCoords()

  for i in range(len(coords)):
    new_coords = translation(coords[i]["x"], coords[i]["y"], x, y)
    coords[i] = {"x": new_coords[0], "y": new_coords[1]}

def zoom(tree_view, sx, sy):
  obj_list, index = tree_view.get_selection().get_selected()
  obj_name = obj_list[index][0]
  obj = display_file.getObject(obj_name)
  coords = obj.getCoords()
  center_point = center(coords)

  for i in range(len(coords)):
    new_coords = scale(coords[i]["x"], coords[i]["y"], sx, sy, center_point["cx"], center_point["cy"])
    coords[i] = {"x": new_coords[0], "y": new_coords[1]}
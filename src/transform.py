import numpy as np
from display_file import DisplayFile

display_file = DisplayFile()

class Transform():
  def translation(self, x, y, dx, dy):
    a = np.array([x, y, 1])
    b = np.array([[1,0,0], [0,1,0], [dx, dy, 1]])
    return a.dot(b)

  def scale(self, x, y, sx, sy, cx, cy):
    a = np.array([x, y, 1])
    b = np.array([[1,0,0],[0,1,0],[-cx, -cy, 1]])
    c = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    d = np.array([[1,0,0],[0,1,0],[cx, cy, 1]])
    
    return a.dot(b).dot(c).dot(d)

  def rotation(self, x, y, dx, dy, degrees):
    sin = np.sin(np.deg2rad(degrees))
    cos = np.cos(np.deg2rad(degrees))
    a = np.array([x, y, 1])
    b = np.array([[1,0,0],[0,1,0],[-dx, -dy, 1]])
    c = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    d = np.array([[1,0,0],[0,1,0],[dx, dy, 1]])
    return a.dot(b).dot(c).dot(d)

  def center(self, coords):
    x = 0
    y = 0
    count = 0
    for i in coords:
      x += i["x"]
      y += i["y"]
      count += 1
    
    return {"cx": x/count, "cy": y/count}

  def move(self, tree_view, x, y):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_name = obj_list[index][0]
    obj = display_file.getObject(obj_name)
    coords = obj.getCoords()

    for i in range(len(coords)):
      new_coords = self.translation(coords[i]["x"], coords[i]["y"], x, y)
      coords[i] = {"x": new_coords[0], "y": new_coords[1]}

  def zoom(self, tree_view, sx, sy):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_name = obj_list[index][0]
    obj = display_file.getObject(obj_name)
    coords = obj.getCoords()
    center_point = self.center(coords)

    for i in range(len(coords)):
      new_coords = self.scale(coords[i]["x"], coords[i]["y"], sx, sy, center_point["cx"], center_point["cy"])
      coords[i] = {"x": new_coords[0], "y": new_coords[1]}

  def rotate(self, tree_view, degrees, rotation_type, x, y):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_name = obj_list[index][0]
    obj = display_file.getObject(obj_name)
    coords = obj.getCoords()
    if(rotation_type == 'center'):
      point = self.center(coords)
    elif(rotation_type == 'world'):
      point = {"cx": 0, "cy": 0}
    else:
      point = {"cx": x, "cy": y}

    for i in range(len(coords)):
      new_coords = self.rotation(coords[i]["x"], coords[i]["y"], point["cx"], point["cy"], degrees)
      coords[i] = {"x": new_coords[0], "y": new_coords[1]}
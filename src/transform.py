import numpy as np
from display_file import DisplayFile

display_file = DisplayFile()

class Transform():
  a,b = -1, 1

  def setWindow(self, window):
    Transform.window = window

  def normalize(self, x, y):
    # x' = (b-a) * ((x - min) / (max - min)) + a
    window = Transform.window
    a,b = self.a, self.b
    wmin_x, wmax_x = window.getMin()["x"], window.getMax()["x"]
    wmin_y, wmax_y = window.getMin()["y"], window.getMax()["y"]

    print("(Transform) Window at ({},{}) ({},{})".format(wmin_x, wmin_y, wmax_x, wmax_y))

    new_x = (b-a) * ((x - wmin_x) / (wmax_x - wmin_x)) + a
    new_y = (b-a) * ((y - wmin_y) / (wmax_y - wmin_y)) + a

    return {"x": new_x, "y": new_y}

  def denormalize(self, x, y):
    # x' = (b-a) * ((x - min) / (max - min)) + a
    window = Transform.window
    a_x, b_x = window.getMin()["x"], window.getMax()["x"]
    a_y, b_y = window.getMin()["y"], window.getMax()["y"]
    
    # print("wmin = ({},{})".format(window.getMin()["x"], window.getMin()["y"]))
    # print("wmax = ({},{})\n".format(window.getMax()["x"], window.getMax()["y"]))

    wmin, wmax = -1, 1

    new_x = (b_x-a_x) * ((x - wmin) / (wmax - wmin)) + a_x
    new_y = (b_y-a_y) * ((y - wmin) / (wmax - wmin)) + a_y

    return {"x": new_x, "y": new_y}

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
    

    print("cx: {} cy: {}".format(x/count, y/count))
    return {"cx": x/count, "cy": y/count}

  def move(self, tree_view, x, y):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_id = obj_list[index][2]
    obj = display_file.getObject(obj_id)
    coords = obj.getWorldCoords()

    for i in range(len(coords)):
      new_coords = self.translation(coords[i]["x"], coords[i]["y"], x, y)
      obj.setWorldCoords(i, new_coords[0], new_coords[1])

  def zoom(self, tree_view, sx, sy):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_id = obj_list[index][2]
    obj = display_file.getObject(obj_id)
    coords = obj.getWorldCoords()
    center_point = self.center(coords)

    for i in range(len(coords)):
      new_coords = self.scale(coords[i]["x"], coords[i]["y"], sx, sy, center_point["cx"], center_point["cy"])
      obj.setWorldCoords(i, new_coords[0], new_coords[1])

  def rotate(self, tree_view, degrees, rotation_type, x, y):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_id = obj_list[index][2]
    obj = display_file.getObject(obj_id)
    coords = obj.getWorldCoords()
    if(rotation_type == 'center'):
      point = self.center(coords)
    elif(rotation_type == 'world'):
      point = {"cx": 0, "cy": 0}
    else:
      point = {"cx": x, "cy": y}

    for i in range(len(coords)):
      new_coords = self.rotation(coords[i]["x"], coords[i]["y"], point["cx"], point["cy"], degrees)
      obj.setWorldCoords(i, new_coords[0], new_coords[1])

import numpy as np
from display_file import DisplayFile
from matrices import Matrices
from variables import clipping_border_size as cbz
from numpy.matlib import identity
from math import sin, cos, pi

display_file = DisplayFile()

class Transform:
  a,b = -1, 1

  def __init__(self):
    self.m = Matrices()

  def setWindow(self, window):
    Transform.window = window

  def normalize(self, x, y):
    # x' = (b-a) * ((x - min) / (max - min)) + a
    window = Transform.window
    a,b = self.a, self.b
    wmin_x, wmax_x = window.getMin()["x"] + cbz, window.getMax()["x"] - cbz
    wmin_y, wmax_y = window.getMin()["y"] + cbz, window.getMax()["y"] - cbz

    # print("(Transform) Window at ({},{}) ({},{})".format(wmin_x, wmin_y, wmax_x, wmax_y))

    new_x = (b-a) * ((x - wmin_x) / (wmax_x - wmin_x)) + a
    new_y = (b-a) * ((y - wmin_y) / (wmax_y - wmin_y)) + a

    return {"x": new_x, "y": new_y}

  def denormalize(self, x, y):
    # x' = (b-a) * ((x - min) / (max - min)) + a
    window = Transform.window
    a_x, b_x = window.getMin()["x"] + cbz, window.getMax()["x"] - cbz
    a_y, b_y = window.getMin()["y"] + cbz, window.getMax()["y"] - cbz
    
    # print("wmin = ({},{})".format(window.getMin()["x"], window.getMin()["y"]))
    # print("wmax = ({},{})\n".format(window.getMax()["x"], window.getMax()["y"]))

    wmin, wmax = -1, 1

    new_x = (b_x-a_x) * ((x - wmin) / (wmax - wmin)) + a_x
    new_y = (b_y-a_y) * ((y - wmin) / (wmax - wmin)) + a_y

    return {"x": new_x, "y": new_y}

  def denormalizeList(self, normalized_coords):
    coords = []
    for i in range(len(normalized_coords)):
      coords.append(self.denormalize(normalized_coords[i]["x"], normalized_coords[i]["y"]))
    return coords

  def normalizeList(self, denormalized_coords):
    coords = []
    for i in range(len(denormalized_coords)):
      coords.append(self.normalize(denormalized_coords[i]["x"], denormalized_coords[i]["y"]))
    return coords

  def translation(self, x, y, dx, dy):
    a = self.m.point(x,y)
    b = self.m.translation(dx, dy)
    
    return a.dot(b)

  def scale(self, x, y, sx, sy, cx, cy):
    a = self.m.point(x,y)
    b = self.m.translation(-cx, -cy)
    c = self.m.scaling(sx, sy)
    d = self.m.translation(cx, cy)
    
    return a.dot(b).dot(c).dot(d)

  def rotation(self, x, y, dx, dy, degrees):
    a = self.m.point(x,y)
    b = self.m.translation(-dx, -dy)
    c = self.m.rotation(degrees)
    d = self.m.translation(dx, dy)
    return a.dot(b).dot(c).dot(d)

  def center(self, coords):
    x = 0
    y = 0
    count = 0
    for i in coords:
      x += i["x"]
      y += i["y"]
      count += 1
    

    # print("cx: {} cy: {}".format(x/count, y/count))
    return {"cx": x/count, "cy": y/count}

  def move(self, tree_view, x, y):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_id = obj_list[index][2]
    obj = display_file.getObject(obj_id)

    if(obj.__class__.__name__ == "Object3D"):
      lista_pontos_3d = []

      for segment in obj.segments:
        lista_pontos_3d.append(segment[0])
        lista_pontos_3d.append(segment[1])

      return self.translacao3d(lista_pontos_3d, x, -y, 0)


    coords = obj.getNormalizedCoords()
    coords_denorm = self.denormalizeList(coords)

    for i in range(len(coords)):
      new_coords = self.translation(coords_denorm[i]["x"], coords_denorm[i]["y"], x, y)
      obj.setWorldCoords(i, new_coords[0], new_coords[1])

  def zoom(self, tree_view, sx, sy):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_id = obj_list[index][2]
    obj = display_file.getObject(obj_id)
    
    if(obj.__class__.__name__ == "Object3D"):
      lista_pontos_3d = []
      x, y, z = obj.get_gravity_center()
      for segment in obj.segments:
        lista_pontos_3d.append(segment[0])
        lista_pontos_3d.append(segment[1])
      return self.escalonamento3d(lista_pontos_3d, 2, x, y, z)
    
    coords = obj.getNormalizedCoords()
    coords_denorm = self.denormalizeList(coords)
    center_point = self.center(coords_denorm)

    for i in range(len(coords)):
      new_coords = self.scale(coords_denorm[i]["x"], coords_denorm[i]["y"], sx, sy, center_point["cx"], center_point["cy"])
      obj.setWorldCoords(i, new_coords[0], new_coords[1])

  def rotate(self, tree_view, degrees, rotation_type, x, y):
    obj_list, index = tree_view.get_selection().get_selected()
    obj_id = obj_list[index][2]
    obj = display_file.getObject(obj_id)
    if(obj.__class__.__name__ == "Object3D"):
      lista_pontos_3d = []
      x, y, z = obj.get_gravity_center()
      for segment in obj.segments:
        lista_pontos_3d.append(segment[0])
        lista_pontos_3d.append(segment[1])
      self.rotacao3d(lista_pontos_3d, 'u',x,y,z)
      return self.rotacao3d(lista_pontos_3d, 'r',x,y,z)

    coords = obj.getNormalizedCoords()
    coords_denorm = self.denormalizeList(coords)
    if(rotation_type == 'center'):
      point = self.center(coords_denorm)
    elif(rotation_type == 'world'):
      point = {"cx": 0, "cy": 0}
    else:
      point = {"cx": x, "cy": y}

    for i in range(len(coords)):
      new_coords = self.rotation(coords_denorm[i]["x"], coords_denorm[i]["y"], point["cx"], point["cy"], degrees)
      obj.setWorldCoords(i, new_coords[0], new_coords[1])

  def calculatePointsBezier(self, coords):
    converted_points = []

    mb = np.array([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]])
    
    t = 0
    i = 0
    while i < len(coords):
        c1x, c2x, c3x, c4x = coords[i + 0]["x"], coords[i + 1]["x"], coords[i + 2]["x"], coords[i + 3]["x"]
        c1y, c2y, c3y, c4y = coords[i + 0]["y"], coords[i + 1]["y"], coords[i + 2]["y"], coords[i + 3]["y"]
        gbx = np.array([[c1x], [c2x], [c3x], [c4x]])
        gby = np.array([[c1y], [c2y], [c3y], [c4y]])
        
        while t < 1:
            xt = np.array([pow(t, 3), pow(t, 2), t, 1])
            temp = xt.dot(mb)
            
            _x = temp.dot(gbx)
            _y = temp.dot(gby)
            
            p = {"x": _x, "y": _y}
            converted_points.append(p)

            t += 0.05
        i = i + 4

    return converted_points

  def calculateBSpline(self, coords):
    converted_points = []
    n_points = 20
    bspline = np.array([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 0, 3, 0], [1, 4, 1, 0]])
    bspline_matrix = np.true_divide(bspline, 6)
    proj_x = np.array([v["x"] for v in coords], dtype=float)
    proj_y = np.array([v["y"] for v in coords], dtype=float)
    for i in range(0, len(coords) - 3):
      Gbs_x = proj_x[i:i + 4]
      Gbs_y = proj_y[i:i + 4]

      Cx = bspline_matrix.dot(Gbs_x)
      Cy = bspline_matrix.dot(Gbs_y)

      Dx = self.fd_matrix(1.0 / n_points).dot(Cx)
      Dy = self.fd_matrix(1.0 / n_points).dot(Cy)
      
      for k in range(n_points + 1):
        x = Dx[0]
        y = Dy[0]
        print(x)
        print(y)
        Dx = Dx + np.append(Dx[1:], 0)
        Dy = Dy + np.append(Dy[1:], 0)

        converted_points.append({"x": x, "y": y})
    print(converted_points)
    return converted_points

  def fd_matrix(self, delta):
    return np.array(
        [
            [0, 0, 0, 1],
            [delta**3, delta**2, delta, 0],
            [6 * delta**3, 2 * delta**2, 0, 0],
            [6 * delta**3, 0, 0, 0]
        ]
    )
  
  def translacao3d(self, pontos3d, tx, ty, tz):
    matriz_transformacao = np.array([[1, 0, 0, 0],
                                     [0, 1, 0, 0],
                                     [0, 0, 1, 0],
                                     [tx, ty, tz, 1]])

    self.transformacao3d(pontos3d, matriz_transformacao)

  def escalonamento3d(self, pontos, mult, tx, ty, tz):
    matriz_escala = np.array([[mult, 0, 0, 0], [0, mult, 0, 0], [0, 0, mult, 0], [0, 0, 0, 1]])
    matriz_centro = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-tx, -ty, -tz, 1]])
    matriz_centro_objeto = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [tx, ty, tz, 1]])
    matriz_transformacao = np.dot(np.dot(matriz_centro, matriz_escala), matriz_centro_objeto)

    self.transformacao3d(pontos, matriz_transformacao)


  def rotacao3d(self, pontos, direcao, tx, ty, tz):
      if direcao == 'l':
          theta = 10 * pi / 180
          eixo = 'y'
      if direcao == 'r':
          theta = - 10 * pi / 180
          eixo = 'y'
      if direcao == 'u':
          theta = 10 * pi / 180
          eixo = 'x'
      if direcao == 'd':
          theta = - 10 * pi / 180
          eixo = 'x'

      identidade = identity(4, dtype=int)
      matriz_rotacao_x = identidade
      matriz_rotacao_y = identidade
      matriz_rotacao_z = identidade

      matriz_centro = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [-tx, -ty, -tz, 1]])

      matriz_centro_objeto = np.array([[1, 0, 0, 0],
                                      [0, 1, 0, 0],
                                      [0, 0, 1, 0],
                                      [tx, ty, tz, 1]])

      if eixo == 'y':
          matriz_rotacao_x = np.array([[1, 0,  0, 0],
                                    [0, cos(0), sin(0), 0],
                                    [0, sin(0), cos(0), 0],
                                    [0, 0, 0, 1]])

          matriz_rotacao_y = np.array([[cos(theta), 0, -sin(theta), 0],
                                      [0, 1, 0, 0],
                                      [sin(theta), 0, cos(theta), 0],
                                      [0, 0, 0, 1]])

          matriz_rotacao_z = np.array([[cos(0),-sin(0), 0, 0],
                                      [sin(0), cos(0), 0, 0],
                                      [0, 0, 1, 0],
                                      [0, 0, 0, 1]])


      if eixo == 'x':

          matriz_rotacao_z = np.array([[cos(theta),-sin(theta), 0, 0],
                                      [sin(theta), cos(theta), 0, 0],
                                      [0, 0, 1, 0],
                                      [0, 0, 0, 1]])

      matriz_transformacao = matriz_centro @ matriz_rotacao_x @ matriz_rotacao_y @ matriz_rotacao_z @ matriz_centro_objeto

      self.transformacao3d(pontos, matriz_transformacao)


  def transformacao3d(self, pontos3d, matriz_transformacao):
      for ponto in pontos3d:
          m = np.array([ponto.x, ponto.y, ponto.z, 1])
          new_point = np.dot(m, matriz_transformacao)
          ponto.x = new_point.flat[0]
          ponto.y = new_point.flat[1]
          ponto.z = new_point.flat[2]


  def perspectiva(self, pontos3d, d):
      M = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                  [0, 0, d, 1]])

      for ponto in pontos3d:
          m = np.array([ponto.x, ponto.y, ponto.z, 1])
          p = m @ M

          ponto.x = p.flat[0] * d / p.flat[2]
          ponto.y = p.flat[1] * d / p.flat[2]
          ponto.z = d
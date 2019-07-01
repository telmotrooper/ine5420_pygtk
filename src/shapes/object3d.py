from shapes.point3d import Point3D
from numpy import array, append
from utils.gen_random_id import generateRandomId
from transform import Transform

class Object3D:
    def __init__(self, _segments: [[Point3D, Point3D]], _name: str = None):
        self.segments = _segments
        self.name = _name
        self.id = generateRandomId()
        self.transform = Transform()

    def get_attributes(self):
        return str(self), self.name

    def __str__(self):
        if len(self.segments) == 1:
            return 'Rect3D'
        return 'Object3D'

    def at(self, index: int):
        return self.segments[index]

    def get_gravity_center(self):
        x = 0
        y = 0
        z = 0
        for segment in self.segments:
            x += (segment[0].x + segment[1].x)/2
            y += (segment[0].y + segment[1].y)/2
            z += (segment[0].z + segment[1].z)/2

        return x / len(self.segments), y / len(self.segments), z / len(self.segments)

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
    
    def getName(self):
      return self.name

    def getId(self):
      return self.id

    def scale(self, percentage):
        x, y, z = self.get_gravity_center()
        lista_pontos_3d = []
        for segment in self.segments:
            lista_pontos_3d.append(segment[0])
            lista_pontos_3d.append(segment[1])
        return self.transform.escalonamento3d(lista_pontos_3d, percentage, x, y, z)
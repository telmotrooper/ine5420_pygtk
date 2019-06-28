from shapes.point3d import Point3D
from numpy import array, append
from utils.gen_random_id import generateRandomId

class Object3D:
    def __init__(self, _segments: [[Point3D, Point3D]], _name: str = None):
        self.segments = _segments
        self.name = _name
        self.id = generateRandomId()

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
        for segmento in self.segments:
            x += (segmento[0].x + segmento[1].x)/2
            y += (segmento[0].y + segmento[1].y)/2
            z += (segmento[0].z + segmento[1].z)/2

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
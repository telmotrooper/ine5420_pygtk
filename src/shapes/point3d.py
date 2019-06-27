from utils.gen_random_id import generateRandomId
class Point3D:
    def __init__(self, _x, _y, _z, _name=None):
        self.x = _x
        self.y = _y
        self.z = _z
        self.name = _name
        self.id = generateRandomId()

    def get_attributes(self):
        return str(self), self.name

    def __str__(self):
        return 'Ponto3d'

    def get_centro_gravidade(self):
        return self.x, self.y, self.z
    
    def getName(self):
      return self.name

    def getId(self):
      return self.id
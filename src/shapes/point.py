import numpy as np
# pylint: disable=no-name-in-module, import-error
from utils.gen_random_id import generateRandomId
from transform import Transform
from shapes.shape import Shape

class Point(Shape):
  def __init__(self, name):
    super().__init__(name)


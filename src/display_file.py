class DisplayFile:
  def __init__(self):
    self.objects = []

  def addObject(self, object):
    self.objects.append(object)

  def getObjects(self):
    return self.objects

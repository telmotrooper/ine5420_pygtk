class DisplayFile:
  def __init__(self):
    self.objects = []

  def addObject(self, object):
    self.objects.append(object)
    print("Object {} added to display file".format(object.getName()))


  def getObjects(self):
    return self.objects

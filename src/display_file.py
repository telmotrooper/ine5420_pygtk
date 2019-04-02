from gi.repository import Gtk

class DisplayFile:
  objects = []
  builder = None
  objectList = None

  def addObject(self, object):
    self.objects.append(object)
    DisplayFile.objectList.append([object.getName(), object.__class__.__name__])

  def getObjects(self):
    return self.objects

  def setBuilder(self, builder):
    DisplayFile.builder = builder
    DisplayFile.objectList = self.builder.get_object("ObjectList")



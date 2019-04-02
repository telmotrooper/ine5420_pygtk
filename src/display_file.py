from gi.repository import Gtk

class DisplayFile:
  objects = []
  builder = None

  def addObject(self, object):
    self.objects.append(object)

  def getObjects(self):
    return self.objects

  def setBuilder(self, builder):
    DisplayFile.builder = builder

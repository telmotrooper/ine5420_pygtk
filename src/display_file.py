from gi.repository import Gtk

class DisplayFile:
  objects = []
  builder = None
  objectList = None

  def addObject(self, object):
    # Add object to display file
    self.objects.append(object)

    # Add entry to object list (interface) and store index
    index = DisplayFile.objectList.append([object.getName(), object.__class__.__name__])

    # Select entry that was just added
    self.builder.get_object("TreeSelection").select_iter(index)


  def getObjects(self):
    return self.objects

  def setBuilder(self, builder):
    DisplayFile.builder = builder
    DisplayFile.objectList = self.builder.get_object("ObjectList")

  def removeObject(self, object_name):
    for i, o in enumerate(DisplayFile.objects):
      if o.name == object_name:
        del DisplayFile.objects[i]
        break

  def getObject(self, object_name):
    for i, o in enumerate(DisplayFile.objects):
      if o.name == object_name:
        return DisplayFile.objects[i]
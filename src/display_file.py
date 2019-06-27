from gi.repository import Gtk

class DisplayFile:
  objects = []
  objects3d = []
  builder = None
  objectList = None

  def addObject(self, obj):
    # Add object to display file
    self.objects.append(obj)

    # Add entry to object list (interface) and store index
    index = DisplayFile.objectList.append([obj.getName(), obj.__class__.__name__, obj.getId()])

    # Select entry that was just added
    self.builder.get_object("TreeSelection").select_iter(index)

  def addObject3d(self, obj):
      # Add object to display file
    self.objects3d.append(obj)

    # Add entry to object list (interface) and store index
    index = DisplayFile.objectList.append([obj.getName(), obj.__class__.__name__, obj.getId()])

    # Select entry that was just added
    self.builder.get_object("TreeSelection").select_iter(index)

  def getObjects(self):
    return self.objects
  
  def getObjects3d(self):
    return self.objects3d

  def setBuilder(self, builder):
    DisplayFile.builder = builder
    DisplayFile.objectList = self.builder.get_object("ObjectList")

  def removeObject(self, object_id):
    for i, o in enumerate(DisplayFile.objects):
      if o.id == object_id:
        del DisplayFile.objects[i]
        break
    
    for i, o in enumerate(DisplayFile.objects3d):
      if o.id == object_id:
        del DisplayFile.objects3d[i]
        break

  def wipeOut(self):
    DisplayFile.objectList.clear()
    for i, o in enumerate(DisplayFile.objects):
      del DisplayFile.objects[i]
    
    for i, o in enumerate(DisplayFile.objects3d):
      del DisplayFile.objects3d[i]

  def getObject(self, object_id):
    for i, o in enumerate(DisplayFile.objects):
      if o.id == object_id:
        return DisplayFile.objects[i]
    
    for i, o in enumerate(DisplayFile.objects3d):
      if o.id == object_id:
        return DisplayFile.objects3d[i]
from display_file import DisplayFile

class ObjHandler:
  def __init__(self):
    self.display_file = DisplayFile()

  def importFile(self, path):
    print("{}".format(path))
    self.file = open(path, "r+")  # read and write

    for line in self.file:
      print(line)
  
  def exportFile(self, path):
    print("Work in progress")

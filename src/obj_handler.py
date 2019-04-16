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
    output_file = open(path, "w+") # write, overwrite and create if needed

    for obj in DisplayFile.objects:
      obj_type = obj.__class__.__name__

      if(obj_type == "Point"):
        w_coords = obj.getWorldCoords()[0]
        output_file.write("o {}\n".format(obj.getName()))
        output_file.write("p {} {} 0\n".format(w_coords["x"], w_coords["y"]))
      
      elif(obj_type == "Line"):
        output_file.write("o {}\n".format(obj.getName()))
        print("Line behavior here")
      elif(obj_type == "Polygon"):
        output_file.write("o {}\n".format(obj.getName()))
        print("Polygon behavior here")

    output_file.write("\n")
    output_file.close()

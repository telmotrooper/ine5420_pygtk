import re

from display_file import DisplayFile

class ObjHandler:
  def __init__(self):
    self.display_file = DisplayFile()

  def importFile(self, path):
    print("{}".format(path))
    vertices = dict()
    vertice_counter = 0

    self.file = open(path, "r+")  # read and write

    for line in self.file:
      if(line[0] == "v"):
        vertice_counter += 1
        vertices[vertice_counter] = line
    
    print(vertices[1])
    temp = re.findall(r"\S+", vertices[1])
    print(temp)

  
  def exportFile(self, path):
    output_file = open(path, "w+") # write, overwrite and create if needed
    temp = "" # this variable holds the objects related to the vertices
    vertice_counter = 0


    # Valid objects are:
    # - vertice (v) (these are always in the beginning of the file)
    # - point (p)
    # - line (l)
    # - object name (o)
    

    for obj in DisplayFile.objects:
      obj_type = obj.__class__.__name__
      w_coords = obj.getWorldCoords()

      if(obj_type == "Point"):
        vertice_counter += 1
        output_file.write("v {} {} 0\n".format(w_coords[0]["x"], w_coords[0]["y"]))
        
        temp += "o {}\n".format(obj.getName())
        temp += "p {}\n".format(vertice_counter)
      
      elif(obj_type == "Line"):
        vertice_counter += 1
        output_file.write("v {} {} 0\n".format(w_coords[0]["x"], w_coords[0]["y"]))
        vertice_counter += 1
        output_file.write("v {} {} 0\n".format(w_coords[1]["x"], w_coords[1]["y"]))
        
        temp += "o {}\n".format(obj.getName())
        temp += "l {} {}\n".format(vertice_counter-1, vertice_counter)
      
      elif(obj_type == "Polygon"):
        temp += "o {}\n".format(obj.getName())
        temp += "l"

        for coord in w_coords:
          vertice_counter += 1
          output_file.write("v {} {} 0\n".format(coord["x"], coord["y"]))
          temp += " {}".format(vertice_counter)

    output_file.write("{}\n".format(temp))
    output_file.close()

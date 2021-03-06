import re

from display_file import DisplayFile
from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from shapes.curve import Curve

class ObjHandler:
  def __init__(self):
    self.display_file = DisplayFile()

  def importFile(self, path):
    self.display_file.wipeOut()
    #print("{}".format(path))
    vertices = dict()
    vertice_counter = 0
    name = ""

    self.file = open(path, "r+")  # read and write

    for line in self.file:
      if(line[0] == "v"): # store vertices in a dictionary
        vertice_counter += 1
        vertices[vertice_counter] = line

      elif(line[0] == "o"): # store temporarily the name of the object to come
        match = re.findall(r"\S+", line)
        name = match[1]
      
      elif(line[0] == "p"): # TODO: FINISH THIS
        match = re.findall(r"\S+", line)
        vertice_for_point = vertices[float(match[1])]
        match = re.findall(r"\S+", vertice_for_point)
        coord = { "x": float(match[1]), "y": float(match[2]) }

        p1 = Point(name)
        p1.addCoords(coord["x"], coord["y"])
        self.display_file.addObject(p1)
      
      elif(line[0] == "l"):
        match = re.findall(r"\S+", line)
        
        if(len(match) == 3):  # line
          l = Line(name)
        else: # polygon
          l = None
          
          if(match[1] == match[-1]):
            l = Polygon(name)
          else:
            l = Curve(name)

        for item in match:
          if(item != "l"):  # ignore the first character, only compute coordinates
            vertice_for_point = vertices[float(item)]
            match_vertice = re.findall(r"\S+", vertice_for_point)
            coord = { "x": float(match_vertice[1]), "y": float(match_vertice[2]) }
            l.addCoords(coord["x"], coord["y"])

        if(match[1] == match[-1]):  # if polygon (last coords == first coords)
          l.popCoords()             # remove repeated coords
        
        self.display_file.addObject(l)
  
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
        initial = vertice_counter + 1
        for coord in w_coords:
          vertice_counter += 1
          output_file.write("v {} {} 0\n".format(coord["x"], coord["y"]))
          temp += " {}".format(vertice_counter)
        temp += " {}\n".format(initial)
      
      elif(obj_type == "Curve"):
        temp += "o {}\n".format(obj.getName())
        temp += "l"
        for coord in w_coords:
          vertice_counter += 1
          output_file.write("v {} {} 0\n".format(coord["x"], coord["y"]))
          temp += " {}".format(vertice_counter)
        temp += "\n"

    output_file.write("{}\n".format(temp))
    output_file.close()

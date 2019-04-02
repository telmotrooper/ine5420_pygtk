from gi.repository import Gtk
from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from display_file import DisplayFile

class Handler:
  def __init__(self, builder, drawing_manager):
    self.builder = builder
    self.dm = drawing_manager

    # References to GTK objects
    self.add_object_window = self.builder.get_object("AddObjectWindow")
    self.text_view = self.builder.get_object("Log")
    self.tree_view = self.builder.get_object("TreeView")

    self.text_buffer = self.text_view.get_buffer()
    self.display_file = DisplayFile()
    self.display_file.setBuilder(builder)

    # Used to keep state of polygon when points are added
    self.temp_polygon = []

  def onDestroy(self, *args):
    Gtk.main_quit()

  def onAddObjectClicked(self, button):
    self.printToLog("onAddObjectClicked")
    add_object_window = self.builder.get_object("AddObjectWindow")
    add_object_window.show_all()

  def onAddPolygonPoint(self, button):
    x_entry = self.builder.get_object("EntryXPolygon").get_text()
    y_entry = self.builder.get_object("EntryYPolygon").get_text()
    self.temp_polygon.append({"x": x_entry, "y": y_entry})
    self.printToLog("onAddPolygonPoint ({},{})".format(x_entry, y_entry))

  def onRemovePolygonPoint(self, button):
    if(len(self.temp_polygon) > 0):
      self.temp_polygon.pop()
    else:
      self.printToLog("No point to remove")
    
    self.printToLog("onRemovePolygonPoint")

  def onAddPolygon(self, button):
    self.printToLog("onAddPolygon")

    name = self.builder.get_object("PolygonName").get_text()
    polygon = Polygon(name)

    for point in self.temp_polygon:
      polygon.addCoords(int(point["x"]), int(point["y"]))

    self.display_file.addObject(polygon)
    self.temp_polygon = []
    self.add_object_window.hide()

  def onAddPoint(self, button):
    self.printToLog("onAddPoint")
    name_entry = self.builder.get_object("PointNameEntry")
    x_entry = self.builder.get_object("PointXEntry")
    y_entry = self.builder.get_object("PointYEntry")
    p1 = Point(name_entry.get_text())

    p1.addCoords(int(x_entry.get_text()), int(y_entry.get_text()))
    self.display_file.addObject(p1)
    self.add_object_window.hide()

  def onAddLine(self, button):
    self.printToLog("onAddLine")
    name_entry = self.builder.get_object("EntryNameNewLine")
    x1_entry = self.builder.get_object("EntryX1Line")
    y1_entry = self.builder.get_object("EntryY1Line")
    x2_entry = self.builder.get_object("EntryX2Line")
    y2_entry = self.builder.get_object("EntryY2Line")

    l1 = Line(name_entry.get_text())
    l1.addCoords(int(x1_entry.get_text()), int(y1_entry.get_text()))
    l1.addCoords(int(x2_entry.get_text()), int(y2_entry.get_text()))

    self.display_file.addObject(l1)
    self.add_object_window.hide()
  
  def onRemoveObjectClicked(self, button):
    self.printToLog("onRemoveObjectClicked")
    obj_list, index = self.tree_view.get_selection().get_selected()
    if index != None:
      self.display_file.removeObject(obj_list[index][0])
      obj_list.remove(index)
      self.dm.redraw()

  def onZoomOut(self, button):
    self.printToLog("onZoomOut")  
    self.dm.getWindow().zoom(0.9)
    self.dm.redraw()

  def onZoomIn(self, button):
    self.printToLog("onZoomIn")  
    self.dm.getWindow().zoom(1.1)
    self.dm.redraw()

  def onMoveWindowUp(self, button):
    self.printToLog("onMoveWindowUp")
    self.dm.getWindow().move(0, 100)
    self.dm.redraw()

  def onMoveWindowDown(self, button):
    self.printToLog("onMoveWindowDown")
    self.dm.getWindow().move(0, -100)
    self.dm.redraw()

  
  def onMoveWindowLeft(self, button):
    self.printToLog("onMoveWindowLeft")
    self.dm.getWindow().move(-100, 0)
    self.dm.redraw()

  
  def onMoveWindowRight(self, button):
    self.printToLog("onMoveWindowRight")
    self.dm.getWindow().move(100, 0)
    self.dm.redraw()


  def printToLog(self, text):
    buffer, view = self.text_buffer, self.text_view
    buffer.insert_at_cursor(text + "\n")
    view.scroll_to_mark(buffer.get_insert(), 0, 0, 0, 0)

from gi.repository import Gtk
from shapes.point import Point
from shapes.line import Line
from display_file import DisplayFile

class Handler:
  def __init__(self, builder, drawingmanager):
    self.builder = builder
    self.drawingmanager = drawingmanager

    # References to GTK objects
    self.add_object_window = self.builder.get_object("AddObjectWindow")
    self.text_view = self.builder.get_object("Log")

    self.text_buffer = self.text_view.get_buffer()
    self.display_file = DisplayFile()

  def onDestroy(self, *args):
    Gtk.main_quit()

  def onZoomOut(self, button):
    self.printToLog("onZoomOut")  

  def onZoomIn(self, button):
    self.printToLog("onZoomIn")  

  def onAddObjectClicked(self, button):
    self.printToLog("onAddObjectClicked")
    add_object_window = self.builder.get_object("AddObjectWindow")
    add_object_window.show_all()

  def onAddPolygonPoint(self, button):
    x_entry = self.builder.get_object("EntryXPolygon").get_text()
    y_entry = self.builder.get_object("EntryYPolygon").get_text()
    self.printToLog("onAddPolygonPoint ({},{})".format(x_entry, y_entry))



  def onAddPolygon(self, button):
    self.printToLog("onAddPolygon")
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

  def onMoveWindowUp(self, button):
    self.printToLog("onMoveWindowUp")

  def onMoveWindowDown(self, button):
    self.printToLog("onMoveWindowDown")
  
  def onMoveWindowLeft(self, button):
    self.printToLog("onMoveWindowLeft")
  
  def onMoveWindowRight(self, button):
    self.printToLog("onMoveWindowRight")

  def printToLog(self, text):
    text_buffer, text_view = self.text_buffer, self.text_view
    text_buffer.insert_at_cursor(text + "\n")
    text_view.scroll_to_mark(text_buffer.get_insert(), 0, 0, 0, 0)


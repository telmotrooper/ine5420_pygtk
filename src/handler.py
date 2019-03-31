from gi.repository import Gtk
from shapes.point import Point
from shapes.line import Line

class Handler:
  def __init__(self, builder):
    self.builder = builder
    self.text_view = self.builder.get_object("Log")
    self.text_buffer = self.text_view.get_buffer()

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

  def onAddPolygon(self, button):
    self.printToLog("onAddPolygon")

  def onAddPoint(self, button):
    self.printToLog("onAddPoint")
    name_entry = self.builder.get_object("PointNameEntry")
    x_entry = self.builder.get_object("PointXEntry")
    y_entry = self.builder.get_object("PointYEntry")
    p1 = Point(name_entry.get_text())
    p1.addCoords(x_entry.get_text(), y_entry.get_text())

  def onAddLine(self, button):
    self.printToLog("onAddLine")
    name_entry = self.builder.get_object("EntryNameNewLine")
    x1_entry = self.builder.get_object("EntryX1Line")
    y1_entry = self.builder.get_object("EntryY1Line")
    x2_entry = self.builder.get_object("EntryX2Line")
    y2_entry = self.builder.get_object("EntryY2Line")
    l1 = Line(name_entry.get_text())
    l1.addCoords(x1_entry.get_text(), y1_entry.get_text())
    l1.addCoords(x2_entry.get_text(), y2_entry.get_text())
  
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
    self.text_buffer.insert_at_cursor(text + "\n")


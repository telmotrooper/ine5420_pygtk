from gi.repository import Gtk
from shapes.curve import Curve
from shapes.point import Point
from shapes.line import Line
from shapes.polygon import Polygon
from shapes.point3d import Point3D
from shapes.object3d import Object3D
from display_file import DisplayFile
from transform import Transform
from obj_handler import ObjHandler
from clipping import Clipping

class Handler:
  def __init__(self, builder, drawing_manager):
    self.builder = builder
    self.dm = drawing_manager
    self.transform = Transform()
    self.obj_handler = ObjHandler()
    self.clipping = Clipping()

    # References to GTK objects
    self.add_object_window = self.builder.get_object("AddObjectWindow")
    self.text_view = self.builder.get_object("Log")
    self.tree_view = self.builder.get_object("TreeView")

    self.obj_file_chooser = self.builder.get_object("ObjFileChooser")
    self.object_radio_button = self.builder.get_object("ObjectRadioButton")
    self.world_radio_button = self.builder.get_object("WorldRadioButton")
    self.point_radio_button = self.builder.get_object("PointRadioButton")
    self.rotate_x = self.builder.get_object("RotateX")
    self.rotate_y = self.builder.get_object("RotateY")
    self.object_rotation_angle = self.builder.get_object("objectRotationAngle")
    self.object_units_for_moving = self.builder.get_object("objectUnitsForMoving")
    self.line_clipping_cs = self.builder.get_object("LineClippingCS")
    self.line_clipping_lb = self.builder.get_object("LineClippingLB")
    self.window_selected = self.builder.get_object("WindowSelected")
    self.object_selected = self.builder.get_object("ObjectSelected")

    self.text_buffer = self.text_view.get_buffer()
    self.display_file = DisplayFile()
    self.display_file.setBuilder(builder)

    # Used to keep state of polygons and curves when points are added
    self.temp_polygon = []
    self.temp_curve = []

  def onDestroy(self, *args):
    Gtk.main_quit()

  def onImportObj(self, button):
    self.printToLog("onImportObj")
    self.obj_file_chooser.show_all()

  def onCancelFileImport(self, button):
    self.printToLog("onCancelFileImport")
    self.obj_file_chooser.hide()

  def onFileClicked(self, button):
    file_path = self.obj_file_chooser.get_filename()
    self.printToLog("onFileClicked ({})".format(file_path))
    self.obj_handler.importFile(file_path)
    self.obj_file_chooser.hide()

  def onExportObj(self, button):
    self.printToLog("onExportObj")
    self.obj_handler.exportFile("./file.obj")

  def onRotateWindowLeft(self, button):
    self.printToLog("onRotateWindowLeft")
    angle =int(self.object_rotation_angle.get_text())
    self.dm.getWindow().rotate(angle)
    self.dm.redraw()

  def onRotateWindowRight(self, button):
    self.printToLog("onRotateWindowRight")
    angle = float(self.object_rotation_angle.get_text())
    self.dm.getWindow().rotate(-angle)
    self.dm.redraw()

  def onAddObjectClicked(self, button):
    self.printToLog("onAddObjectClicked")
    add_object_window = self.builder.get_object("AddObjectWindow")
    add_object_window.show_all()

  def onAddCurvePoint(self, button):
    x_entry = self.builder.get_object("EntryXCurve").get_text()
    y_entry = self.builder.get_object("EntryYCurve").get_text()
    self.temp_curve.append({"x": x_entry, "y": y_entry})
    self.printToLog("onAddCurvePoint ({},{})".format(x_entry, y_entry))

  def onAddPolygonPoint(self, button):
    x_entry = self.builder.get_object("EntryXPolygon").get_text()
    y_entry = self.builder.get_object("EntryYPolygon").get_text()
    self.temp_polygon.append({"x": x_entry, "y": y_entry})
    self.printToLog("onAddPolygonPoint ({},{})".format(x_entry, y_entry))

  def onRemoveCurvePoint(self, button):
    if(len(self.temp_curve) > 0):
      self.temp_curve.pop()
    else:
      self.printToLog("No point to remove")
    
    self.printToLog("onRemoveCurvePoint")

  def onRemovePolygonPoint(self, button):
    if(len(self.temp_polygon) > 0):
      self.temp_polygon.pop()
    else:
      self.printToLog("No point to remove")
    
    self.printToLog("onRemovePolygonPoint")

  def onAddCurve(self, button):
    self.printToLog("onAddCurve")

    name = self.builder.get_object("CurveName").get_text()
    curve = Curve(name)

    for point in self.temp_curve:
      curve.addCoords(float(point["x"]), float(point["y"]))

    self.display_file.addObject(curve)
    self.temp_curve = []
    self.add_object_window.hide()

  def onAddPolygon(self, button):
    self.printToLog("onAddPolygon")

    name = self.builder.get_object("PolygonName").get_text()
    polygon = Polygon(name)

    for point in self.temp_polygon:
      polygon.addCoords(float(point["x"]), float(point["y"]))

    self.display_file.addObject(polygon)
    self.temp_polygon = []
    self.add_object_window.hide()

  def onAddCube(self, button):
    segmentosobj = [[Point3D(50, 50, 0), Point3D(50, 100, 0)],
                    [Point3D(50, 100, 0), Point3D(150, 100, 0)],
                    [Point3D(150, 100, 0), Point3D(150, 50, 0)],
                    [Point3D(150, 50, 0), Point3D(50, 50, 0)],
                    [Point3D(50, 50, 50), Point3D(50, 100, 50)],
                    [Point3D(50, 100, 50), Point3D(150, 100, 50)],
                    [Point3D(150, 100, 50), Point3D(150, 50, 50)],
                    [Point3D(150, 50, 50), Point3D(50, 50, 50)],
                    [Point3D(50, 50, 0), Point3D(50, 50, 50)],
                    [Point3D(50, 100, 0), Point3D(50, 100, 50)],
                    [Point3D(150, 100, 0), Point3D(150, 100, 50)],
                    [Point3D(150, 50, 0), Point3D(150, 50, 50)]]

    obj3d = Object3D(segmentosobj, 'primeiro obj 3d')
    self.display_file.addObject3d(obj3d)

  def onAddPoint(self, button):
    self.printToLog("onAddPoint")
    name_entry = self.builder.get_object("PointNameEntry")
    x_entry = self.builder.get_object("PointXEntry")
    y_entry = self.builder.get_object("PointYEntry")
    p1 = Point(name_entry.get_text())

    p1.addCoords(float(x_entry.get_text()), float(y_entry.get_text()))
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
    l1.addCoords(float(x1_entry.get_text()), float(y1_entry.get_text()))
    l1.addCoords(float(x2_entry.get_text()), float(y2_entry.get_text()))

    self.display_file.addObject(l1)
    self.add_object_window.hide()
  
  def onRemoveObjectClicked(self, button):
    self.printToLog("onRemoveObjectClicked")
    obj_list, index = self.tree_view.get_selection().get_selected()
    if index != None:
      self.display_file.removeObject(obj_list[index][2])
      obj_list.remove(index)
      self.dm.redraw()
    else:
      self.printToLog("No object selected")

  def onZoomOut(self, button):
    self.printToLog("onZoomOut")  
    self.dm.getWindow().zoom(0.9)
    self.dm.redraw()

  def onZoomIn(self, button):
    self.printToLog("onZoomIn")  
    self.dm.getWindow().zoom(1.1)
    self.dm.redraw()

  def onMoveObjectUp(self, button):
    if self.window_selected.get_active():
      return self.onMoveWindowUp(button)
    
    units = float(self.object_units_for_moving.get_text())
    self.printToLog("onMoveObjectUp")
    self.transform.move(self.tree_view, 0, units)
   
    self.dm.redraw()

  def onMoveObjectDown(self, button):
    if self.window_selected.get_active():
      return self.onMoveWindowDown(button)

    units = float(self.object_units_for_moving.get_text())
    self.printToLog("onMoveObjectDown")
    self.transform.move(self.tree_view, 0, -units)
    self.dm.redraw()

  def onMoveObjectLeft(self, button):
    if self.window_selected.get_active():
      return self.onMoveWindowLeft(button)

    units = float(self.object_units_for_moving.get_text())
    self.printToLog("onMoveObjectLeft")
    self.transform.move(self.tree_view, -units, 0)
    self.dm.redraw()

  def onMoveObjectRight(self, button):
    if self.window_selected.get_active():
      return self.onMoveWindowRight(button)
    
    units = float(self.object_units_for_moving.get_text())
    self.printToLog("onMoveObjectRight")
    self.transform.move(self.tree_view, units, 0)
    self.dm.redraw()

  def onLineClippingChanged(self, button):
    if self.line_clipping_cs.get_active():
      self.printToLog("Line clipping algorithm set to Cohen-Sutherland.")
      self.clipping.setlineClippingAlgorithm("cs")
    elif self.line_clipping_lb.get_active():
      self.printToLog("Line clipping algorithm set to Liang-Barsky.")
      self.clipping.setlineClippingAlgorithm("lb")

  def onRotateObjectLeft(self, button):
    if self.window_selected.get_active():
      return self.onRotateWindowLeft(button)

    self.printToLog("onRotateObjectLeft")
    angle =int(self.object_rotation_angle.get_text())

    if self.object_radio_button.get_active():
      self.transform.rotate(self.tree_view, -angle, 'center',0,0)
    elif self.world_radio_button.get_active():
      self.transform.rotate(self.tree_view, -angle, 'world',0,0)
    elif self.point_radio_button.get_active():
      x = float(self.rotate_x.get_text())
      y = float(self.rotate_y.get_text())
      self.transform.rotate(self.tree_view, -angle, 'point',x,y)
    self.dm.redraw()

  def onRotateObjectRight(self, button):
    if self.window_selected.get_active():
      return self.onRotateWindowRight(button)

    self.printToLog("onRotateObjectRight")
    angle =int(self.object_rotation_angle.get_text())
    
    if self.object_radio_button.get_active():
      self.transform.rotate(self.tree_view, angle, 'center',0,0)
    elif self.world_radio_button.get_active():
      self.transform.rotate(self.tree_view, angle, 'world',0,0)
    elif self.point_radio_button.get_active():
      x = float(self.rotate_x.get_text())
      y = float(self.rotate_y.get_text())
      self.transform.rotate(self.tree_view, angle, 'point',x,y)

    self.dm.redraw()
  
  def onScaleObjectUp(self, button):
    if self.window_selected.get_active():
      return self.onZoomIn(button)
    
    self.printToLog("onScaleObjectUp")
  
    self.transform.zoom(self.tree_view, 2, 2)
    self.dm.redraw()

  def onScaleObjectDown(self, button):
    if self.window_selected.get_active():
      return self.onZoomOut(button)
    
    self.printToLog("onScaleObjectDown")
    self.transform.zoom(self.tree_view, 0.5, 0.5)
    self.dm.redraw()

  def onMoveWindowUp(self, button):
    self.printToLog("onMoveWindowUp")
    units = float(self.object_units_for_moving.get_text())
    self.dm.getWindow().move(0, units)
    self.dm.redraw()

  def onMoveWindowDown(self, button):
    self.printToLog("onMoveWindowDown")
    units = float(self.object_units_for_moving.get_text())
    self.dm.getWindow().move(0, -units)
    self.dm.redraw()

  
  def onMoveWindowLeft(self, button):
    self.printToLog("onMoveWindowLeft")
    units = float(self.object_units_for_moving.get_text())
    self.dm.getWindow().move(-units, 0)
    self.dm.redraw()

  
  def onMoveWindowRight(self, button):
    self.printToLog("onMoveWindowRight")
    units = float(self.object_units_for_moving.get_text())
    self.dm.getWindow().move(units, 0)
    self.dm.redraw()


  def printToLog(self, text, end = "\n"):
    buffer, view = self.text_buffer, self.text_view
    buffer.insert_at_cursor(text + end)
    view.scroll_to_mark(buffer.get_insert(), 0, 0, 0, 0)

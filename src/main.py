#!/usr/bin/env python3

import gi
import cairo
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from handler import Handler
from drawing_manager import DrawingManager
from display_file import DisplayFile

def main():
  builder = Gtk.Builder()
  builder.add_from_file("gui.glade")

  window_object = builder.get_object("MainWindow")
  window_object.set_icon_from_file("icon.png")
  window_object.show_all()

  # Prevent these dialogs from being destroyed on close (they just hide)
  add_object_window = builder.get_object("AddObjectWindow")
  obj_file_chooser = builder.get_object("ObjFileChooser")
  add_object_window.connect("delete-event", lambda w, e: w.hide() or True)
  obj_file_chooser.connect("delete-event", lambda w, e: w.hide() or True)

  drawing_area = builder.get_object("DrawingArea")
  dm = DrawingManager(drawing_area)
  drawing_area.connect("draw", dm.draw)

  builder.connect_signals(Handler(builder, dm))

  Gtk.main()

# Get absolute path from relative path
def get_resource_path(rel_path):
    dir_of_py_file = os.path.dirname(__file__)
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource

if __name__ == "__main__":
  main()

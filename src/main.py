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
  window_object.show_all()

  add_object_window = builder.get_object("AddObjectWindow")
  add_object_window.connect("delete-event", lambda w, e: w.hide() or True)

  drawing_area = builder.get_object("DrawingArea")
  dm = DrawingManager(drawing_area)
  drawing_area.connect("draw", dm.draw)

  builder.connect_signals(Handler(builder, dm))

  Gtk.main()

if __name__ == "__main__":
  main()

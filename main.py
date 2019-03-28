#!/usr/bin/env python3

import gi
import cairo
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from handler import Handler

def main():
  builder = Gtk.Builder()
  builder.add_from_file("gui.glade")
  builder.connect_signals(Handler(builder))

  window = builder.get_object("MainWindow")
  window.show_all()

  drawing_area = builder.get_object("DrawingArea")
  drawing_area.connect("draw", draw)

  Gtk.main()

def draw(da, ctx):
  # draw background
  ctx.set_source_rgb(255, 255, 255) # color white
  ctx.paint()

  ctx.set_source_rgb(0, 0, 0) # color black
  
  ctx.set_line_width(2)
  ctx.move_to(20, 20)
  ctx.rel_line_to(50,50)
  ctx.stroke()

if __name__ == "__main__":
  main()

#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from handler import Handler

def main():
  builder = Gtk.Builder()
  builder.add_from_file("gui.glade")
  builder.connect_signals(Handler(builder))

  window = builder.get_object("MainWindow")
  window.show_all()

  Gtk.main()

if __name__ == "__main__":
  main()

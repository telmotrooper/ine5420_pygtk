from gi.repository import Gtk

class Handler:
  def __init__(self, builder):
    self.builder = builder
    self.text_view = self.builder.get_object("Log")
    self.text_buffer = self.text_view.get_buffer()

  def onDestroy(self, *args):
    Gtk.main_quit()

  def onAddObjectClicked(self, button):
    self.printToLog("onAddObjectClicked")
    add_object_window = self.builder.get_object("AddObjectWindow")
    add_object_window.show_all()

  def onRemoveObjectClicked(self, button):
    self.printToLog("onRemoveObjectClicked")

  def printToLog(self, text):
    self.text_buffer.insert_at_cursor(text + "\n")


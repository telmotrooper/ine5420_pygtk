class Handler:
  def __init__(self, builder):
    self.builder = builder

  def onDestroy(self, *args):
    Gtk.main_quit()

  def onButtonPressed(self, button):
    print("Hello World!")
  
  def openAddObjectWindow(self, button):
    add_object_window = self.builder.get_object("AddObjectWindow")
    add_object_window.show_all()
  
  def openAddObjectWindow(self, button):
    add_object_window = self.builder.get_object("AddObjectWindow")
    add_object_window.show_all()

from gi.repository import Gedit, GObject
from geditpyflakes.plugin import PyflakesPlugin

class Geditpyflakes(GObject.Object, Gedit.WindowActivatable):
	__gtype_name__ = "GeditpyflakesInstance"

	window = GObject.property(type=Gedit.Window)

	def __init__(self):
		GObject.Object.__init__(self)

	def _get_instance(self):
		return self.window.get_data(self.__gtype_name__)

	def _set_instance(self, instance):
		self.window.set_data(self.__gtype_name__, instance)

	def do_activate(self):
		self._set_instance(PyflakesPlugin(self.window))

	def do_deactivate(self):
		self._get_instance().do_deactivate()
		self._set_instance(None)

	def do_update_state(self):
		self._get_instance().do_update_state()

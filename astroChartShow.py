#!/usr/bin/env python3
"""
# https://docs.gtk.org/gtk4/
# https://pygobject.gnome.org/tutorials/gtk4.html
# https://discourse.gnome.org/t/scaling-images-with-cairo-is-much-slower-in-gtk4/7701
# https://blog.gtk.org/2018/03/16/textures-and-paintables/
"""
#basics
import math, sys, os.path, datetime, socket, gettext, codecs, webbrowser, pytz

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
from gi.repository import GLib, Gio, Gtk, Gdk, GObject

# This would typically be its own file
MENU_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
<menu id="menubar">
  <submenu>
    <attribute name="label" translatable="yes">Application</attribute>
    <section>
      <item>
        <attribute name="action">win.maximize</attribute>
        <attribute name="label" translatable="yes">Maximize</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="action">win.about</attribute>
        <attribute name="label" translatable="yes">_About</attribute>
      </item>
      <item>
        <attribute name="action">app.quit</attribute>
        <attribute name="label" translatable="yes">_Quit</attribute>
      </item>
    </section>
  </submenu>
  <submenu>
    <attribute name="label" translatable="yes">Zoom</attribute>
    <item>
      <attribute name="label" translatable="yes">In</attribute>
      <attribute name="action">win.zoom</attribute>
      <attribute name="target">zIn</attribute>
    </item>
    <item>
      <attribute name="label" translatable="yes">80%</attribute>
      <attribute name="action">win.zoom</attribute>
      <attribute name="target">z80</attribute>
    </item>
    <item>
      <attribute name="label" translatable="yes">100%</attribute>
      <attribute name="action">win.zoom</attribute>
      <attribute name="target">z100</attribute>
    </item>
    <item>
      <attribute name="label" translatable="yes">150%</attribute>
      <attribute name="action">win.zoom</attribute>
      <attribute name="target">z150</attribute>
    </item>
    <item>
      <attribute name="label" translatable="yes">200%</attribute>
      <attribute name="action">win.zoom</attribute>
      <attribute name="target">z200</attribute>
    </item>
    <item>
      <attribute name="label" translatable="yes">Out</attribute>
      <attribute name="action">win.zoom</attribute>
      <attribute name="target">zOut</attribute>
    </item>
  </submenu>
</menu>
</interface>
"""

APPLICATION_ID = "org.openastro.AstroApp"
#for debugging set to True
LOCAL = False
OFFSET = 64
RATIO = math.sqrt(2)
VERSION = "1.1.90"

class ViewSVG(Gtk.Widget):
	def __init__(self, path, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# loads now SVG files, Pixbuf not needed anymore
		self.setupSVG(path)

	def setupSVG(self, path):
		self.texture = Gdk.Texture.new_from_filename(path)
		self.scale = 1

	def do_snapshot(self, snapshot):
		width = self.texture.get_intrinsic_width() * self.scale
		height = self.texture.get_intrinsic_height() * self.scale
		self.texture.snapshot(snapshot, width, height)

	def do_get_request_mode(self):
		return Gtk.SizeRequestMode.CONSTANT_SIZE

	def do_measure(self, orientation, for_size):
		if orientation == Gtk.Orientation.HORIZONTAL:
			width = self.texture.get_intrinsic_width() * self.scale
			return (width, width, -1, -1)
		else:
			height = self.texture.get_intrinsic_height() * self.scale
			return (height, height, -1, -1)

class AstroWindow(Gtk.ApplicationWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# By default the title bar will be hide, let's show it
		self.props.show_menubar = True
		# This will be in the windows group and have the 'win' prefix
		max_action = Gio.SimpleAction.new_stateful(
			"maximize", None, GLib.Variant.new_boolean(False)
		)
		max_action.connect("change-state", self.on_maximize_toggle)
		self.add_action(max_action)

		# Keep it in sync with the actual state
		self.connect(
			"notify::maximized",
			lambda obj, _pspec: max_action.set_state(
				GLib.Variant.new_boolean(obj.props.maximized)
			),
		)

		about_action = Gio.SimpleAction.new("about", None)
		about_action.connect("activate", self.about_callback)
		self.add_action(about_action)


		zoom_action = Gio.SimpleAction.new_stateful("zoom", GLib.VariantType.new('s'), GLib.Variant.new_string('zIn'))
		zoom_action.connect("activate", self.zoom_callback)
		self.add_action(zoom_action)
		app.set_accels_for_action(detailed_action_name="win.zoom::zIn", accels=["<Ctrl>plus"])
		app.set_accels_for_action(detailed_action_name="win.zoom::z100", accels=["<Ctrl>1"])
		app.set_accels_for_action(detailed_action_name="win.zoom::zOut", accels=["<Ctrl>minus"])
		box = Gtk.Box()
		self.set_child(box)
		scrolled_window = Gtk.ScrolledWindow()
		self.image = ViewSVG("openAstroChart.svg")
		self.image.set_vexpand(True)
		self.image.set_hexpand(True)
		self.image.set_valign(Gtk.Align.CENTER)
		self.image.set_halign(Gtk.Align.CENTER)
		scrolled_window.set_child(self.image)
		box.append(scrolled_window)

	def on_change_label_state(self, action, value):
		action.set_state(value)
		self.label.set_text(value.get_string())

	def on_maximize_toggle(self, action, value):
		action.set_state(value)
		if value.get_boolean():
			self.maximize()
		else:
			self.unmaximize()

	""" Menu 'Zoom' """
	def zoom_callback(self, action, parameter):
		""" check for zoom level and draw """
		z_level = parameter.get_string()
		action.set_state(parameter)
		#action.set_state(parameter)
		ratio = self.image.scale
		if z_level == 'zIn':
			self.image.scale += 0.1
		elif z_level == 'z80':
			self.image.scale = 0.8
		elif z_level == 'z100':
			self.image.scale = 1.0
		elif z_level == 'z150':
			self.image.scale = 1.5
		elif z_level == 'z200':
			self.image.scale = 2.0
		elif z_level == 'zOut':
			if ratio >= 0.2:
				self.image.scale -= 0.1
			else:
				return
		self.image.queue_resize()

	# callback function for about (see the AboutDialog example)
	def about_callback(self, action, parameter):
		about = Gtk.AboutDialog(transient_for=self, modal=True)
		about.set_logo(Gdk.Texture.new_from_filename('about.xpm'));
		#about.connect("response", lambda w,e: about.destroy())
		#about.connect("close", lambda w,e: about.destroy())
		about.set_program_name("Gtk4 OpenAstro.org - Open Source Astrology")
		about.set_size_request(480, -1)
		about.set_version('Gtk4 Version ' + VERSION)
		about.set_authors(["Pelle van der Scheer, Amsterdam / The Netherlands"])
		documenters = ["Erich Küster, Krefeld / Nortrhine-Westfalia / Germany"]
		about.set_copyright("Copyright © 2012-2026 Pelle van der Scheer. All rights reserved.")
		with open('COMMENTS', "r") as f:
			comments = f.read()
		about.set_comments(comments)
		with open('LICENSE', "r") as f:
			license = f.read()
		about.set_license(license)
		about.set_website("https://pygobject.gnome.org/tutorials/gtk4.html");
		about.set_website_label("GTK4 — PyGObject")
		# show the aboutdialog
		about.present()

	# a callback function to destroy the aboutdialog
	def on_close(self, action, parameter):
		self.close()

class Application(Gtk.Application):
	def __init__(self, *args, **kwargs):
		super().__init__(
			*args,
			application_id=APPLICATION_ID,
			flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
			**kwargs,
		)
		display = Gdk.Display.get_default()
		monitor = display.get_primary_monitor()
		geometry = monitor.get_geometry()
		self.screen_width = geometry.width
		self.screen_height = geometry.height
		#calculate available screen size
		#correct dimensions
		self.height = self.screen_height-OFFSET
		self.width = self.height * RATIO
		self.window = None

		self.add_main_option(
			"local",
			ord("l"),
			GLib.OptionFlags.NONE,
			GLib.OptionArg.NONE,
			"AstroChart Standakone",
			None,
		)

	def do_startup(self):
		Gtk.Application.do_startup(self)

		quit_action = Gio.SimpleAction.new("quit", None)
		quit_action.connect("activate", self.on_quit)
		self.add_action(quit_action)
		self.set_accels_for_action("app.quit", ["<Primary>Q"])
		#action='win.zoom',  target_value=GLib.Variant('s', 'z80')
		builder = Gtk.Builder.new_from_string(MENU_XML, -1)
		self.set_menubar(builder.get_object("menubar"))

	def do_activate(self):
		# We only allow a single window and raise any existing ones
		if self.window is None:
			# Windows are associated with the application
			# when the last one is closed the application shuts down
			self.window = AstroWindow(application=self, title="AstroChart Window")
		self.window.set_default_size(self.width, self.height)
		self.window.present()

	def do_command_line(self, command_line):
		options = command_line.get_options_dict()
		# convert GVariantDict -> GVariant -> dict
		options = options.end().unpack()
		if "local" in options:
			LOCAL = True
			# This is printed on the main instance
			print('OPTION local is', LOCAL)
			pass
		self.activate()
		return 0

	def on_quit(self, _action, _param):
		self.quit()

app = Application()
exit_status = app.run(sys.argv)
sys.exit(exit_status)


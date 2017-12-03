# -*- coding: UTF-8 -*-
# This example is contributed by Martin Enlund
# Example modified for Atom
# Shortcuts Provider was inspired by captain nemo extension

from gettext import gettext, textdomain
from subprocess import PIPE, call
from urllib import unquote
from urlparse import urlparse

from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Gio, GObject, Gtk, Nautilus


COMMAND = "atom"
KEYBINDINGS = "com.github.atom.Keybindings"
GSETTINGS_OPEN_TERMINAL = "nautilus-open"
textdomain("atom")
_ = gettext

def run(file_):
  if file_:
    filename = Gio.File.new_for_uri(file_.get_uri()).get_path()
    if filename:
      call('{0} "{1}" &'.format(COMMAND, filename), shell=True)
    else:
      call("{0} &".format(COMMAND), shell=True)


class OpenAtomShortcutProvider(GObject.GObject,
                                Nautilus.LocationWidgetProvider):

  def __init__(self):
    source = Gio.SettingsSchemaSource.get_default()
    if source.lookup(KEYBINDINGS, True):
      self._gsettings = Gio.Settings.new(KEYBINDINGS)
      self._gsettings.connect("changed", self._bind_shortcut)
      self._create_accel_group()
    self._window = None
    self._uri = None

  def _create_accel_group(self):
    self._accel_group = Gtk.AccelGroup()
    shortcut = self._gsettings.get_string(GSETTINGS_OPEN_TERMINAL)
    key, mod = Gtk.accelerator_parse(shortcut)
    self._accel_group.connect(key, mod, Gtk.AccelFlags.VISIBLE,
                              self._open_terminal)

  def _bind_shortcut(self, gsettings, key):
    if key == GSETTINGS_OPEN_TERMINAL:
      self._accel_group.disconnect(self._open_terminal)
      self._create_accel_group()

  def _open_terminal(self, *args):
    filename = unquote(self._uri[7:])
    run(filename)

  def get_widget(self, uri, window):
    self._uri = uri
    if self._window:
      self._window.remove_accel_group(self._accel_group)
    if self._gsettings:
      window.add_accel_group(self._accel_group)
    self._window = window
    return None


class OpenAtomExtension(GObject.GObject, Nautilus.MenuProvider):

  def _open_terminal(self, file_):
    run(file_)

  def _menu_activate_cb(self, menu, file_):
    self._open_terminal(file_)

  def _menu_background_activate_cb(self, menu, file_):
    self._open_terminal(file_)

  def get_file_items(self, window, files):
    if len(files) != 1:
      return
    items = []
    file_ = files[0]
    print("Handling file: ", file_.get_uri())
    print("file scheme: ", file_.get_uri_scheme())

    if file_:
      filename = file_.get_name().decode('utf-8')
      item = Nautilus.MenuItem(name='NautilusPython::open_file_item',
                               label=_(u'Open In Atom'),
                               tip=_(u'Open Atom For {}').format(filename))
      item.connect('activate', self._menu_activate_cb, file_)
      items.append(item)

    return items

  def get_background_items(self, window, file_):
    items = []

    item = Nautilus.MenuItem(name='NautilusPython::open_bg_file_item',
                             label=_(u'Open Atom Here'),
                             tip=_(u'Open Atom In This Directory'))
    item.connect('activate', self._menu_background_activate_cb, file_)
    items.append(item)
    return items

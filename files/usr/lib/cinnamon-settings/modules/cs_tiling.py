#!/usr/bin/env python

from SettingsWidgets import *
from gi.repository import Gio, Gtk, GObject, Gdk

class Module:
    def __init__(self, content_box):
        keywords = _("window, tile, flip, tiling, snap, snapping")
        advanced = False
        sidePage = SidePage(_("Window Tiling and Edge Flip"), "tiling.svg", keywords, advanced, content_box)
        self.sidePage = sidePage
        self.name = "tiling"
        self.category = "prefs"

        sidePage.add_widget(GSettingsCheckButton(_("Enable Window Tiling and Snapping"), "org.cinnamon.overrides", "edge-tiling", None))
        box = IndentedHBox()
        box.add(GSettingsSpinButton(_("Tiling HUD visibility threshold"), "org.cinnamon.muffin", "tile-hud-threshold", "org.cinnamon.overrides/edge-tiling", 1, 300, 1, 1, _("Pixels")))
        sidePage.add_widget(box, True)

        sidePage.add_widget(GSettingsCheckButton(_("Enable Edge Flip"), "org.cinnamon", "enable-edge-flip", None))
        box = IndentedHBox()
        box.add(GSettingsSpinButton(_("Edge Flip delay"), "org.cinnamon", "edge-flip-delay", "org.cinnamon/enable-edge-flip", 1, 3000, 1, 1, _("ms")))
        sidePage.add_widget(box, True)

#!/usr/bin/env python2
# -*- coding: utf8 -*-

"""
    notify.py: Send notification status messages through libnotify.
"""

#==============================================================================
# Send notification status messages through libnotify.
#==============================================================================

#==============================================================================
#    Copyright 2010 joe di castro <joe@joedicastro.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#==============================================================================

__author__ = "joe di castro <joe@joedicastro.com>"
__license__ = "GNU General Public License version 3"
__date__ = "14/05/2012"
__version__ = "0.3"

# Notify it's not essential and libnotify it's not always installed (in Ubuntu
# & Debian it's optional) but it's very useful to show popup messages
try:
    import pynotify
    import gtk
    import textwrap
    import os
    NOT_NOTIFY = False
except ImportError:
    NOT_NOTIFY = True


def notify(title, msg, icon=None, wrap=None):
    """Send notification icon messages through libnotify.

    Parameters:

    (str) title -- The notification title
    (str) msg -- The message to display into notification
    (str / uri) icon -- Type of icon (ok|info|error|warm|ask|sync) or icon file

    """
    if NOT_NOTIFY:
        return
    if not pynotify.is_initted():
        pynotify.init(title)
    gtk_icon = {'ok': gtk.STOCK_YES,
                'info': gtk.STOCK_DIALOG_INFO,
                'error': gtk.STOCK_DIALOG_ERROR,
                'warm': gtk.STOCK_DIALOG_WARNING,
                'ask': gtk.STOCK_DIALOG_QUESTION,
                'sync': gtk.STOCK_JUMP_TO}
    if wrap:
        msg = os.linesep.join(textwrap.wrap(msg, wrap))
    try:
        note = pynotify.Notification(title, msg)
        helper = gtk.Button()
        gtk_icon = helper.render_icon(gtk_icon[icon], gtk.ICON_SIZE_BUTTON)
        note.set_icon_from_pixbuf(gtk_icon)
    except KeyError:
        note = pynotify.Notification(title, msg, icon)
    try:
        note.show()
    except Exception, e:
        print(e)


def main():
    """Main section"""
    notify('TEST', 'This is an Ok Message', 'ok')
    notify('TEST', 'This is an Info Message', 'info')
    notify('TEST', 'This is an Error Message', 'error')
    notify('TEST', 'This is a Warm Message', 'warm')
    notify('TEST', 'This is an Ask Message', 'ask')
    notify('TEST', 'This is an Sync Message', 'sync')
    notify('TEST', 'This is a Personalized Icon Message',
           '/usr/share/icons/gnome/scalable/places/ubuntu-logo.svg')
    notify('TEST',
           '''
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
           ''', wrap=60)


if __name__ == "__main__":
    main()

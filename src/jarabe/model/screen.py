# Copyright (C) 2006-2008 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging

import dbus


_HARDWARE_MANAGER_INTERFACE = 'org.freedesktop.ohm.Keystore'
_HARDWARE_MANAGER_SERVICE = 'org.freedesktop.ohm'
_HARDWARE_MANAGER_OBJECT_PATH = '/org/freedesktop/ohm/Keystore'

_ohm_service = None


def _get_ohm():
    global _ohm_service
    if _ohm_service is None:
        bus = dbus.SystemBus()
        proxy = bus.get_object(_HARDWARE_MANAGER_SERVICE,
                               _HARDWARE_MANAGER_OBJECT_PATH,
                               follow_name_owner_changes=True)
        _ohm_service = dbus.Interface(proxy, _HARDWARE_MANAGER_INTERFACE)

    return _ohm_service


def set_dcon_freeze(frozen):
    try:
        _get_ohm().SetKey('display.dcon_freeze', frozen)
    except dbus.DBusException:
        logging.error('Cannot unfreeze the DCON')

#!/usr/bin/env python3
# Based on: https://gist.github.com/eacousineau/63651e498ddc31a7c1478f8638d0fd2e
from collections import namedtuple

from gi.repository import GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop

from print import print_notification_receipt

# Similary to `dnotify` package.
BUS = "org.freedesktop.Notifications"
OBJECT = "/org/freedesktop/Notifications"
IFACE = "org.freedesktop.Notifications"

# For the "Notify" event (see references above).
KEYS = (
    "app_name",
    "replaces_id",
    "app_icon",
    "summary",
    "body",
    "actions",
    "hints",
    "expire_timeout",
)

CallKey = namedtuple("CallKey", ("sender", "dest", "serial"))


def notification(summary, body):
    print_notification_receipt(title=summary, message=body)


def main():
    def on_call(message):
        kwargs = dict(zip(KEYS, message.get_args_list()))
        summary = str(kwargs["summary"])
        body = str(kwargs["body"])
        notification(summary, body)

    def on_any(bus, message):
        if (message.get_interface() == IFACE
                and message.get_member() == "Notify"):
            on_call(message)

    dbus_loop = DBusGMainLoop()
    bus = dbus.SessionBus(mainloop=dbus_loop)
    bus.add_match_string_non_blocking("eavesdrop=true")
    bus.add_message_filter(on_any)

    main_loop = GLib.MainLoop()
    print("Now listening for notifications")
    main_loop.run()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from argparse import ArgumentTypeError, ArgumentParser
from os.path import exists, join, normpath
from os import geteuid, stat
import re
import stat as stat_consts
from sys import argv
from typing import NamedTuple

"""
Inspiration taken from:
https://github.com/ahoneybun/keyboard-color-chooser/blob/master/keyboard-color-switcher.py
https://www.howtogeek.com/687970/how-to-run-a-linux-program-at-startup-with-systemd/

Example file /etc/systemd/system/system76-kb-backlight.service:
(because I'm assuming you want this to run on boot.)
(Don't forget to enable the service.)
(Wrap in systemd-cat for proper logging.)
```
[Unit]
Description=Set color and brightness of system-76 laptop keyboard backlight

[Service]
Type=simple
ExecStart=systemd-cat /home/username/.local/bin/set_system76_kb_backlight -c FF1100 -B 15

[Install]
WantedBy=multi-user.target
```
"""

color_hex_regex = re.compile(
    r"""^[0x\\#&uh+]* # Ignore leading prefix characters.
        ([0-9a-f]{2}) # 2 digits for red...
        ([0-9a-f]{2}) # etc
        ([0-9a-f]{2})
        [x\\#&uh+]*$  # Ignore trailing suffix characters, not including 0.""",
    flags = re.I | re.X
)

class Percent:
    def __init__(self, value):
        self.val = int(value)
        if not 0 <= self.val <= 100:
            raise ArgumentTypeError(f'Value "{value}" out of bounds: 0-100.')

    def byte(self):
        return int(self.val * 255 / 100)

    def __str__(self):
        return f'{self.val}%'

class RGB(NamedTuple):
    red: int
    green: int
    blue: int

    def __str__(self):
        return "{red:02X}{green:02X}{blue:02X}".format(
            red=self.red, green=self.green, blue=self.blue
        )
    
def rgb(string):
    match = color_hex_regex.fullmatch(string)
    if match:
        return RGB(red=int(match.group(1), 16),
                   green=int(match.group(2), 16),
                   blue=int(match.group(3), 16))
    else:
        raise ArgumentTypeError(f'"{string}" is not a valid hex color code.')

def get_config_or_die():
    arg_parse = ArgumentParser(
        description="Set the color and brightness of the system76 keyboard backlight.",
        epilog="Most args should be integers in the range 0-100.\n"
               "Color (-c) trumps channels (-r, -g, -b).\n"
    )
    arg_parse.add_argument('-r', '--red',
                           help="The red RGB value.",
                           default=Percent(0),
                           type=Percent)
    arg_parse.add_argument('-g', '--green',
                           help="The green RGB value.",
                           default=Percent(0),
                           type=Percent)
    arg_parse.add_argument('-b', '--blue',
                           help="The blue RGB value.",
                           default=Percent(0),
                           type=Percent)
    arg_parse.add_argument('-c', '--color',
                           help="The RGB hex value. (six digits, common suffixes and prefixes will be dropped)",
                           default=None,
                           type=rgb)
    arg_parse.add_argument('-B', '--brightness',
                           help="The brightness.",
                           default=Percent(19),
                           type=Percent)
    arg_parse.add_argument('-q', '--quiet',
                           help="Supress print statements.",
                           action='store_false',
                           dest='verbose')
    args = arg_parse.parse_args()
    brightness = args.brightness.byte()
    color = (args.color
             if args.color is not None
             else RGB(red=args.red.byte(),
                      green=args.green.byte(),
                      blue=args.blue.byte()))
    log_action = print if args.verbose else lambda *_, **__: None
    return color, brightness, log_action, arg_parse.exit

def be_root_and_installed_for_root_or_die(exit):
    if 0 != geteuid():
        exit(2, "This script has to write to root-only files, so you have to be root to run it.\n")
    self_path_stats = [stat(path) for path in (__file__, argv[0])]
    for result in self_path_stats:
        if (0 != result.st_uid) or (
            result.st_mode & (stat_consts.S_IWGRP | stat_consts.S_IWOTH)
        ):
            exit(2, "This script is expected to run, automatically, as root.\n"
                    "It would be insecure for it to be modifiable by anyone but root.\n"
                    "Use chown and chmod so only the owner, root, can write.\n")


def set_backlight_or_die(brightness, color, exit):
    def valid_abs_path(*p):
        path = normpath('/' + join(*p))
        return path if exists(path) else None

    possible_led_dirs = [
        ('sys', 'class', 'leds', 'system76_acpi::kbd_backlight'),
        ('sys', 'class', 'leds', 'system76::kbd_backlight')
    ]
    led_dir = next((d for d in possible_led_dirs if valid_abs_path(*d)), None)
    if led_dir is None:
        exit(2, "Unable to find the LED control paths.\n")

    color_regions = ('color_left', 'color_center', 'color_right', 'color_extra')
    settings = {
        key: str(value)
        for (key, value)
        in [(valid_abs_path(*led_dir, 'brightness'), brightness),
            *[(valid_abs_path(*led_dir, region), color)
              for region in color_regions]]
        if key is not None
    }
    if len(settings) < 1:
        exit(2, "Unable to find the LED control files.\n")

    for (p,s) in settings.items():
        with open(p, 'w') as f:
            f.write(s)

def main():
    color, brightness, log, exit = get_config_or_die()
    be_root_and_installed_for_root_or_die(exit)
    log("Attempting to set system76 keyboard backlight color and brightness.")
    set_backlight_or_die(brightness, color, exit)
    log("Successfully set system76 keyboard backlight brightness.")
    exit(0)

if __name__ == '__main__':
    main()

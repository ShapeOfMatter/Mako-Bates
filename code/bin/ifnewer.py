#!/usr/bin/env python3

import argparse as ag
from glob import iglob
from operator import itemgetter
import os.path as path
import re
import subprocess

def removeprefix(s, p):
    return s[len(p):] if s.startswith(p) else s

arg_parse = ag.ArgumentParser(description="Run some command if a source file is newer than a dependent file.")
arg_parse.add_argument('-v', '--verbose', action="store_true", help="Print out a drescription of what you're doing.")
arg_parse.add_argument('source', help="The parent file that's being checked for updates.")
arg_parse.add_argument('-d', '--dest',
                       help="The dependent or destination file. May use * wildcards, in which case the youngest match will be used. Default: source.*")
arg_parse.add_argument('-t', '--temp',
                       help="""The "temporary" directory for the dependendent file. Will _not_ be created. Default: .temp in the path of the source""")
arg_parse.add_argument('-c', '--confirm', action="store_true",
                       help="Ask the user for confirmation before actually running the command.")
arg_parse.add_argument('command', nargs='+',  # nargs=ag.REMAINDER,
                       help="The command to run. Will interpret {s} as a placeholder for the source, and {d} as a placeholder for the destination.")
arg_parse.usage = (
    removeprefix(arg_parse.format_usage(), 'usage: ')
    + "  (It's recommended to separate command from the rest of the arguments with -- , to avoid ambiguity.)"
)
args = arg_parse.parse_args()

verbose = args.verbose

def print_if_verbose(s, *, override=False):
    if verbose or override:
        print(s)

backup_split_regex = re.compile(r"""\*  # star
                                   |\?  # or question mark
                                   |\[  # or square brackets
                                       (?!  # containing one or more characters that do not match
                                           (?<!\\)\]  # a close bracket that's not preceeded by a slash
                                       ).+
                                    \]""",
                                re.VERBOSE)
def find_youngest(pattern):
    match_ages = ((name, path.getmtime(name))
                  for name
                  in iglob(pattern)
                  if path.isfile(name))
    return next(
        iter(sorted(match_ages, key=itemgetter(1), reverse=True)),
        ('_'.join(filter(bool, backup_split_regex.split(pattern))) + 'temp', 0.0)
    )

source_placeholder = re.compile(r"""(?<!\\){s}""", re.VERBOSE)  #negative lookbehind to allow \ escaping
dest_placeholder = re.compile(r"""(?<!\\){d}""", re.VERBOSE)  #negative lookbehind to allow \ escaping
def apply_placeholders(fragment, s, d):
    return source_placeholder.sub(s,
                                  dest_placeholder.sub(d,
                                                       fragment))

source = args.source
dest = args.dest
temp_dir = args.temp
confirm = args.confirm
command_pattern = args.command

source_path, source_full_name = path.split(source)
source_first_name, source_extension = path.splitext(source_full_name)
source_date = path.getmtime(source)
found_dest, dest_date = find_youngest(path.join(
    *([temp_dir]
      if temp_dir
      else [source_path, '.temp']),
    (dest if dest else source_first_name + ".*")
))

command = [apply_placeholders(f, source, found_dest) for f in command_pattern]

print_if_verbose(f"""    Source: {source}
    Source Last Modified: {source_date}
    Using Destination: {found_dest}
    Destination Last Modified: {dest_date}
    Ask For Confirmation: {confirm}
    Processed Command: {command}""")

if dest_date < source_date:
    print_if_verbose("Source file was more recently modified.")
    if (not confirm) or (not input(f"Press enter to run '{' '.join(command)}'. (entering text will abort)  ")):
        print_if_verbose("Running Command...")
        cp = subprocess.run(command)
        print_if_verbose(f"Command finished with exit status {cp.returncode}.", override=(0 != cp.returncode))
    else:
        print_if_verbose("Aborted.")
else:
    print_if_verbose("Doing nothing.")





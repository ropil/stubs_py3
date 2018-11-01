#!/usr/bin/env python3
# <imports here>

'''
 {one line to give the program's name and a brief idea of what it does.}
 Copyright (C) 2018  Robert Pilstål

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

# Version and license information
def get_version_str():
    return "\n".join([
        "{project}  Copyright (C) 2018  Robert Pilstål;",
        "This program comes with ABSOLUTELY NO WARRANTY.",
        "This is free software, and you are welcome to redistribute it",
        "under certain conditions; see supplied General Public License."
        ])


# Library functions


# Main; for callable scripts
def main():
    from argparse import ArgumentParser
    from sys import argv, stdin
    parser = ArgumentParser(
        description="{one line to give a brief idea of what the program does.}")
    parser.add_argument(
        "-a", action="store_true", default=False, help="Prints nothing")
    parser.add_argument(
        "-t", nargs=1, default=["nothing"], metavar="TEXT",
        help="What to print")
    parser.add_argument('-v', '--version', action='version',
                        version=get_version_str())
    parser.add_argument(
        "files", nargs="*", metavar="FILE", help="Files for input")
    arguments = parser.parse_args(argv[1:])
    files = arguments.files
    # Use stdin if no supplied files
    if len(arguments.files) == 0:
        files = [stdin]
    
    # Set variables here
    
    # Parse STDIN or files
    for f in files:
        infile = f
        # Open for reading if file path specified
        if isinstance(f, str):
            infile = open(f, 'r')
        for line in infile:
            print(line)
        infile.close()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# <imports here>

'''
 {one line to give the program's name and a brief idea of what it does.}
 Copyright (C) 2018  Robert Pilstål

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
'''

# Version and license information
def get_version_str():
    return "\n".join([
        "{project}  Copyright (C) 2018  Robert Pilstål;",
        "This program comes with ABSOLUTELY NO WARRANTY.",
        "This is free software, and you are welcome to redistribute it",
        "under certain conditions; See the supplied Apache License,",
        "Version 2.0 for the specific language governing permissions",
        "and limitations under the License.",
        "    http://www.apache.org/licenses/LICENSE-2.0"
        ])


#library functions go here


#main definition for callable scripts
def main():
    import argparse
    import sys
    parser = argparse.ArgumentParser(
        description="{one line to give a brief idea of what the program does.}")
    parser.add_argument("-a", action="store_true", default=False,
                        help="Prints nothing")
    parser.add_argument("-t", nargs=1, default=["nothing"], metavar="TEXT",
                        help="What to print")
    parser.add_argument('-v', '--version', action='version', version=get_version_str())
    parser.add_argument("files", nargs="*", metavar="FILE",
                        help="Files for input")
    arguments = parser.parse_args(sys.argv[1:])
    if arguments.a:
        print("Printing " + str(arguments.t[0]))

    #if called from command line
if __name__ == '__main__':
    main()

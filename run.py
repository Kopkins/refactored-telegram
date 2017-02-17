#!/usr/bin/env python3

import sys
import getopt
import railroad


def main():
    help_string = 'septa_tool.py --count <num>'
    # Set expected options and parse
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hc:',['help','count='])
    except getopt.GetoptError:
        print(help_string)
        sys.exit(2)

    # Use arguments and flags to set program parameters
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_string)

    t = railroad.tool()
    t.run_main_menu()


if __name__ == '__main__':
    main()

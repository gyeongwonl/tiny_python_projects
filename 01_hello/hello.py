#!/usr/bin/env python
"""
Author: Gwon Lee
Purpose: Say hello
"""

import argparse


def get_args():
    """ Get the command-line arguments """

    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--name', 
                        metavar='name',
                        default='World', 
                        help='name to greet')
    return parser.parse_args()


def main():
    """" main """

    args = get_args()
    name = args.name
    print("Hello, " + name + "!")


if __name__ == '__main__':
    main()

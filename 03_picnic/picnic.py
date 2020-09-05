#!/usr/bin/env python
"""
Author : Gwon
Date   : 2020-09-05
Purpose: Chapter 3
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Chapter 3',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='item',
                        nargs='+',  # number of items needs to be 1 or more
                        help='Items we are bringing')

    parser.add_argument('-s',
                        '--sorted',
                        help='Whether to sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Solve Chapter 3"""

    args = get_args()
    items = args.items
    num_items = len(items)

    if args.sorted:
        items.sort()

    if num_items == 1:
        lst = items[0]
    elif num_items == 2:
        lst = ' and '.join(items)
    else:
        lst = ", ".join(items[:-1]) + ", and " + items[-1]
    
    print(f"You are bringing {lst}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()

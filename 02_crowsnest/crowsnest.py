#!/usr/bin/env python
"""
Author : Gwon
Date   : 2020-09-02
Purpose: Chpater 2
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Chapter 2',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Solve Chapter 2"""

    args = get_args()
    word = args.word
    vowels = { 'a', 'e', 'i', 'o', 'u' }
    article = 'an' if word[0].lower() in vowels else 'a'

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python
"""
Author : Gwon <Gwon@localhost>
Date   : 2020-09-09
Purpose: Chapter 4
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Chapter 4',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Chapter 4"""

    args = get_args()
    text = args.text
    
    jumper = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0',
            '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}
    #for i in range(10):
    #    if i in {0, 5}:
    #        jumper[i] = abs(i - 5)
    #    else:
    #        jumper[i] = 10 - i

    new_text = ''
    for c in text:
        #i = ord(c) - ord('0')
        #new_text += jumper.get(i, c)
        new_text += jumper.get(c, c)

    print(new_text)
    #print(args.text.translate(str.maketrans(jumper)))


# --------------------------------------------------
if __name__ == '__main__':
    main()

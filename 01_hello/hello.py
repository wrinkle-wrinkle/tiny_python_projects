#!/usr/bin/env python3
"""
Author: John Moses
Purpose: Say Hello
"""

import argparse


def get_args():
    """ Get command-line strings """
    parser = argparse.ArgumentParser(description='Say hello!')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """ main """

    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()

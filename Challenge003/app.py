#!/usr/bin/env python3
"""
created: 2022-03-14 20:58:57
@author: seraph★776
contact: seraph776@gmail.com
project: The Little Book of Programming Challenges
details: Challenge 3
"""


def get_length():
    user_input = int(input('Enter length:\n> '))
    return user_input


def get_width():
    user_input = int(input('Enter width:\n> '))
    return user_input


def get_area():
    length = get_length()
    width = get_width()
    return length * width


def main():
    area = get_area()
    print(f'The area of the rectangle is {area} sq ft.')


if __name__ == '__main__':
    main()

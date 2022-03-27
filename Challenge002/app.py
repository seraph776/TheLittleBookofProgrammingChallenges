#!/usr/bin/env python3
"""
created: 2022-03-14 20:20:26
@author: seraph★776
contact: seraph776@gmail.com
project: The Little Book of Programming Challenges
details: Challenge 2
"""


def get_name():
    user_input = input('What is your name? ')
    return f'Hello {user_input.title()}!'


def main():
    print(get_name())


if __name__ == '__main__':
    main()





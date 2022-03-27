#!/usr/bin/env python3
"""
created: 2022-03-27 16:00:23
@author: seraph★776
contact: seraph776@gmail.com
project: The Little Book of Programming Challenges
details: Challenge 4
"""
import sys


def get_speed():
    user_input = int(input('Please enter the speed:\n>> '))
    return user_input


def get_time():
    user_input = int(input('Please enter the time:\n>> '))
    return user_input


def get_distance():
    result = get_speed() * get_time()
    return result


def quit_program():
    user_input = input('Would you like to quit the game:\n(yes or no) ')
    match user_input:
        case 'yes':
            return True
        case 'no':
            return False
        case _:
            print('Invalid input')
            return quit_program()


def main():
    while True:
        distance = get_distance()
        print(f'The total distance is {distance} miles.\n')
        if quit_program():
            print('Goodbye!')
            sys.exit()
        else:
            main()


if __name__ == '__main__':
    main()

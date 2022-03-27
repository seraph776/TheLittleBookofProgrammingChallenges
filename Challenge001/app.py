#!/usr/bin/env python3
"""
created: 2022-03-14 19:17:28
@author: seraph★776
contact: seraph776@gmail.com
project: The Little Book of Programming Challenges
details: Challenge 1
"""

import unittest
from random import shuffle


def tell_joke(s):
    return '\033[92m' + s + '\033[0m'


def punchline(s):
    return '\033[1;91m' + s + '\033[0m'


def display_jokes(lst):
    for i, item in enumerate(lst, start=1):
        print(f'>> Joke #{i}:')
        joke = item[0]
        punch_line = item[1]
        print(tell_joke(joke))
        input('Press enter to continue... ')
        print(f'{punchline(punch_line)}\n')
    print('End of jokes!')


def main():
    jokes = [
        ('What is the spider such a good computer programmer?', 'It knows all about the web.'),
        ('Why does the computer keep coughing?', 'It has a virus.'),
        ('What does a baby computer call his father?', 'Data'),
        ('What are laptops favourite snacks?', 'Computer chips.'),
        ('How does a computer eat computer chips?', 'With mega-bytes.'),
        ('What did the spider do on the computer?', 'They both have lots of memory.'),
        ('What is an alien\'s favourite key on a keyboard?', 'The space bar.'),
        ('Where did the software developer go?!', 'I don’t know, he ransomware!'),
        ('what do you call a creepy IT teacher?', 'a PDF file'),
        ('Bill Gates teaches a kindergarten class to count to ten:',
         '1, 2, 3, 3.1, 95, 98, ME, 2000, XP, Vista, 7, 8, 10.'),
        ('I started a band called 999 megabytes...', 'we still haven’t gotten a gig.'),
        ('What did the processor say when it was being overclocked?', 'Stop it! It hertz so much!'),
    ]
    shuffle(jokes)
    display_jokes(jokes)


print(main())


if __name__ == '__main__':
    main()


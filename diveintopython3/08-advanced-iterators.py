# re.findall(' s.*? s', "The sixth sick sheikh's sixth sheep's sick.")
# [' sixth s', " sheikh's s", " sheep's s"]
# Because it doesn’t return overlapping matches. The first match overlaps with the second, so the first is returned and the second is skipped. Then the third overlaps with the fourth, so the third is returned and the fourth is skipped. Finally, the fifth is returned. Three matches, not five.

# Using a generator expression instead of a list comprehension can save both cpu and ram. If you’re building an list just to throw it away (e.g. passing it to tuple() or set()), use a generator expression instead!

import re
import itertools

def solve(puzzle):
    ''' an incredible Python cryptarithms or alphametics solver originally written by Raymond Hettinger. ''''
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)

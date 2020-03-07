=========================================================
>>> pattern = '''
    ^                   # ROMAN NUMBERS: beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''
>>> re.search(pattern, 'M', re.VERBOSE)
=========================================================
>>> phonePattern = re.compile(r'''
                # USA TELEPHONE NUMBERS: don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
>>> phonePattern.search('work 1-(800) 555.1212 #1234').groups() ①
('800', '555', '1212', '1234')
=========================================================
^ matches the beginning of a string.
$ matches the end of a string.
\b matches a word boundary.
\d matches any numeric digit.
\D matches any non-numeric character.
x? matches an optional x character (in other words, it matches an x zero or one times).
x* matches x zero or more times.
x+ matches x one or more times.
x{n,m} matches an x character at least n times, but not more than m times.
(a|b|c) matches exactly one of a, b or c.
(x) in general is a remembered group. You can get the value of what matched by using the groups() method of the object returned by re.search.

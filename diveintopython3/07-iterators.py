# The __init__() method is called immediately after an instance of the class is created.
# It would be tempting — but technically incorrect — to call this the “constructor” of the class.
# It’s tempting, because it looks like a C++ constructor (by convention, the __init__() method is the first method defined for the class),
# acts like one (it’s the first piece of code executed in a newly created instance of the class), and even sounds like one.
# Incorrect, because the object has already been constructed by the time the __init__() method is called,
# and you already have a valid reference to the new instance of the class.

class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

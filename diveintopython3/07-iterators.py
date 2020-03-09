# The __init__() method is called immediately after an instance of the class is created.
# It would be tempting — but technically incorrect — to call this the “constructor” of the class.
# It’s tempting, because it looks like a C++ constructor (by convention, the __init__() method is the first method defined for the class),
# acts like one (it’s the first piece of code executed in a newly created instance of the class), and even sounds like one.
# Incorrect, because the object has already been constructed by the time the __init__() method is called,
# and you already have a valid reference to the new instance of the class.
# ====================================================================================
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

# ====================================================================================
class LazyRules:
    '''Iterator for pluralization rules for English words 
    
    '''
    
    rules_filename = 'plural6-rules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(
            pattern, search, replace)
        self.cache.append(funcs)
        return funcs

rules = LazyRules()


# We have achieved pluralization nirvana.
# Minimal startup cost. The only thing that happens on import is instantiating a single class and opening a file (but not reading from it).
# Maximum performance. The previous example would read through the file and build functions dynamically every time you wanted to pluralize a word. This version will cache functions as soon as they’re built, and in the worst case, it will only read through the pattern file once, no matter how many words you pluralize.
#Separation of code and data. All the patterns are stored in a separate file. Code is code, and data is data, and never the twain shall meet.
# ☞Is this really nirvana? Well, yes and no. Here’s something to consider with the LazyRules example: the pattern file is opened (during __init__()), and it remains open until the final rule is reached. Python will eventually close the file when it exits, or after the last instantiation of the LazyRules class is destroyed, but still, that could be a long time. If this class is part of a long-running Python process, the Python interpreter may never exit, and the LazyRules object may never get destroyed.
# There are ways around this. Instead of opening the file during __init__() and leaving it open while you read rules one line at a time, you could open the file, read all the rules, and immediately close the file. Or you could open the file, read one rule, save the file position with the tell() method, close the file, and later re-open it and use the seek() method to continue reading where you left off. Or you could not worry about it and just leave the file open, like this example code does. Programming is design, and design is all about trade-offs and constraints. Leaving a file open too long might be a problem; making your code more complicated might be a problem. Which one is the bigger problem depends on your development team, your application, and your runtime environment.

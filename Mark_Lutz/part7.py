# Exceptions
# try/except
# try/finally
# raise
# assert
# with/as
# except Exception
# try/except/else/finally

class MyError(Exception): pass

def stuff(file):
    raise MyError()

file = open ('data' , 'w')  # may fail here

try:
    stuff(file)  # Exception MyError is generated
finally:
    file.close ()  # cleanup phase

print('not reached')  # MyError will be propagated

# try must have either except OR finally

# raise new-exception from other Exception

try:
   try:
      raise IndexError ()
   except Exception as E :
      raise TypeError () from E
except Exception as E :
   raise SyntaxError () from E

# raise from None

assert test, data
# "equals" to
if __debug__:
    if not test:
        raise AssertionError (data)

# python -O main.py => Optimized run with __debug__ = False
def f (х) :
    assert х < 0, 'х must be negative'
    return х ** 2

import asserter
asserter.f(1)

with decimal.localcontext() as ctx:  # import decimal
    ctx.prec = 2
    x = decimal.Decimal('1.00')/decimal.Decimal('3.00')

class TraceBlock:
    def message(self , arg) :
        print (' running ' + arg)
    def __ enter __ (self) :
        print (' starting with block')
        return self
    def __ exit __ (self, exc_type, exc_value, exc_tb) :
        if exc_type is None:
            print (' exited normally! ') # normal exit
        else :
            print ('raise an exception! ' + str (exc_type) ) # generated Exception
        return False # propagated
if __ name __ == ' __ main __ ' :
    with TraceBlock () as action:
        action.message (' test 1')
        print (' reached' ) 
    with TraceBlock () as action:
        action.message (' test 2')
        raise TypeError
        print('not reached') 

# OOP Exceptions
class General(Exception) : pass
class Specificl(General) : pass
class Specific2(General) : pass

def raiserO () :
    X = General ()  # superclass
    raise X
def raiserl ():
    X = Specificl ()  # instance/subclass
    raise X
def raiser2 ():
    X = Specific2()  # instance/subclass
    raise X

for func in (raiserO, raiserl, raiser2):
    try:
        func ()
    except General: # match superclass
        import sys
        print (' caught : %s ’ % sys . exc_info ()[0])

# __str__/__repr__ of Exceptions
class Е (Exception) :
    def __ repr __ (self) : return 'Not called! ' # is not called !!!!

>>> raise E('spam')
main __ . E: spam

class E (Exception) :
    def __ str __ (self) : return 'Called? ' # called

>>> raise E('spam')
__ main __ .E: Called!

# nested try/except - program flow returns to the previous except level (one level)
# nested try/finally - program flow goes through every level on finally (or until matching except)

# higher exceptions hooks - https://docs.python.org/3/library/atexit.html

# OR sys.excepthooк

import sys
log = open ('testlog', 'a')
from testapi import moreTests, runNextTest, testName
def testdriver():
    while moreTests():
        try:
            runNextTest()
        except:
            print ('FAILED' , testName(), sys.exc_info()[:2], file=log)
        else:
            print ('PASSED' , testName(), file=log)
testdriver()

#
import traceback
def inverse(x):
    return 1 / x
try:
    inverse (0)
except Exception:
    traceback.print_exc(file=open('badly.exc', 'w'))
print('Bye')

# PyDoc/PyLint/PyChecker
# PyUnit(unittest)/doctest

# python -m profile main.py

import sys, locale
>>> sys.platform
>>> locale.getpreferredencoding(False), sys.getdefaultencoding()

>>> set (dir('abc')) - set(dir(b'abc'))
{'isprintable', 'format', 'isdecimal', 'encode', 'format_map' , 'casefold', ' isidentifier ', 'isnumeric'}
>>> set(dir(b'abc')) - set(dir('abc'))
{'fromhex', 'decode', 'hex'}

# PROPERTIES

attribute = property(fget, fset, fdel, doc)

class Person:
    def __init__ (self, name):
        self._name = name
    def getName(self):
        print ('fetch ...')
        return self, name
    def setName(self, value):
        print ('change ...')
        self._name = value
    def delName(self):
        print ('remove ...')
        del self._name
    name = property(getName, setName, delName, "name property docs")


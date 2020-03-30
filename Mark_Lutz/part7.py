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

class Descriptor:
    def __get__ (self, instance, owner):
        print (self, instance, owner, sep='\n')
class Subject:
    attr = Descriptor()

>>>X = Subject ()
>>>X.attr
<__main__.Descriptor object at 0x03AD1990>
<__main__.Subject object at 0x03AD1970>
<class '__main__.Subject'>

# X.attr -> Descriptor.__get__(Subject.attr, X, Subject)

class D:
    def __get__ (*args) : print ('get')
    def __set__ (*args) : raise AttributeError ('cannot set')

# __delete__ (__delattr__) <> __del__  !!!


class Name:
    "name descriptor docs"
    def __get__(self, instance, owner) :
        print (' fetch ...')
        return instance._name
    def __set__(self, instance, value) :
        print ( ’ change . . . ')
        instance._name = value
    def __delete__(self, instance) :
        print (' remove ...')
        del instance._name
class Person:
    def __init__ (self, name) :
        self._name = name
    name = Name ()


# nested descriptor
class Person:
    def __init__(self, name):
        self._name = name

    class Name:                                 # Using a nested class
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change...')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name
    name = Name()


# desc-state-desc.py
class DescState:                           # Use descriptor state, (object) in 2.X
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner):    # On attr fetch
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value):    # On attr assign
        print('DescState set')
        self.value = value

# Client class
class CalcAttrs:
    X = DescState(2)                       # Descriptor class attr
    Y = 3                                  # Class attr
    def __init__(self):
        self.Z = 4                         # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                 # X is computed, others are not
obj.X = 5                                  # X assignment is intercepted
CalcAttrs.Y = 6                            # Y reassigned in class
obj.Z = 7                                  # Z assigned in instance
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()                         # But X uses shared data, like Y!
print(obj2.X, obj2.Y, obj2.Z)


def __getattr__ (self, name) : # unknown attributes [obj. паше]
def __getattribute__ (self, name) : # all attributes [obj .name]
def __setattr__ (self, name, value) : # all attributes [obj .name=value]
def __delattr__ (self, name) : # all attributes [del obj.name]

def __getattribute__ (self, name):  # WRONG
    x = self.other

def __getattribute__ (self, name) :  # CORRECT
    x = object.__getattribute__ (self, 'other') 

def __getattribute__ (self, name) :  # WRONG
    x = self.__dict__ ['other']

def __setattr__ (self, name, value) :  # CORRECT
    object.__setattr__(self, name, value)
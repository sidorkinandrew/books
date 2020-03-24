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

# OOP Exce[tions
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

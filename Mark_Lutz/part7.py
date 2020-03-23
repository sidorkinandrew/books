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

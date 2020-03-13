# https://docs.python.org/2.5/whatsnew/pep-343.html
from contextlib import contextmanager

@contextmanager
def db_transaction (connection):
    cursor = connection.cursor()
    try:
        yield cursor
    except:
        connection.rollback()
        raise
    else:
        connection.commit()

db = DatabaseConnection()
with db_transaction(db) as cursor:
    ...

#
class DatabaseConnection:
    ...
    def __exit__ (self, type, value, tb):
        if tb is None:
            # No exception, so commit
            self.commit()
        else:
            # Exception occurred, so rollback.
            self.rollback()
            # return False


# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

files = []

for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')
        
# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
from contextlib import ContextDecorator

class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False

@makeparagraph()
def emit_html():
    print('Here is some non-HTML')

emit_html()

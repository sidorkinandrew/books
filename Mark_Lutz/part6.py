>>> x.age # Но извлечение атрибута проверяет также классы
>>> x. __ dict __ ['age 1'] # Индексирование словаря не производит поиск в иерархии наследования
>>> х. __ class __ # Связь экземпляра с классом
>>> гес. __ bases __ # Связь с суперклассами

# Fetching all methods/properties - use __class__ and then ___dict__, then __dict__ against all __bases__ 
# OR use dir(obj)
>>> len(dir(bob) )
32
>>> list (name for name in dir (bob) if not name, start s with (' __ '))
['gatherAttrs', 'giveRaise', 'job', 'lastName', 'name', 'pay']

# __some_method - pseudo-closed attributes of a class if dundered in front
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted (self.__dict__):
            attrs.append('{} = {}'.format(key, getattr(self,key)))
        return ', '.join(attrs)
    def __repr__ (self):
        return '[{}: {}]'.format(self.__class__.__name__, self.gatherAttrs())

# using shelves
import shelve
with shelve.open('persondb') as db:
    for obj in (bob):
        db[obj.name] = obj

# __rep___ useful to  any class
    def __repr__ (self):
        attrs = []
        for key in sorted (self.__dict__):
            attrs.append('{} = {}'.format(key, getattr(self,key)))
        return '[{}: {}]'.format(self.__class__.__name__, ', '.join(attrs))

# instance.method(*args) == class.method(instance, *args)

# LEGB name resolution search not CLEGB!

def class_tree(classname, indent):
"""
recursive super class name search
"""
    print("."*indent, classname.__name__)
    for superclass in classname.__bases__:
        class_tree(superclass, indent+3)

def show_instance_tree(class_instance):
    print("Building tree for {}".format(class_instance))
    class_tree(class_instance.__class__, 3)

def selftest ():
    class A: pass
    class В(A): pass
    class C(A): pass
    class D(В, C) : pass
    class E: pass
    class F(D,E) : pass
    show_instance_tree(B())
    show_instance_tree(F())

if __name__ == '__main__': selftest()

# python -3 -m time it -n 1000 -r 5 -s "L = list(range (100))" "x = L.__len__()"

class Indexer:
    def __getitem__ (self, index) :
        if isinstance(index, int) : # Проверка режима использования
            print (' indexing ', index)
        else:
            print (' slicing' , index.start, index.stop, index.step)

# Но метод __ index __ в Python З.Х не имеет отношения к индексированию!!!!

class Stepper Index:
    def getitem (self, i) :
        return self.data[i]
# in, [], () = X, list, tuple, join

# __iter__ + yield / skips an element
class SkipObject: 
    def __init__ (self, wrapped) : # local
        self.wrapped = wrapped # local state
    def __iter__ (self) :
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item

# __contains__ > __iter__ > __next__ > __getitem__

# self.attribute = value => self.__setattr__('attribute' , vaule)

# __getattr__  is called for non-extent attributes (those who were not found via class_tree_search)

# __str__ => str, print => user-friendly

# __repr__ => all contexts => dev-friendly

# __call__ 

# __bool__ >= __len__

# def/lambda | __call__ | bound_function | classmethod | staticmethod


# p. 190 - factories
def factory(aClass, *pargs, **kargs):
    return aClass(*pargs, **kargs)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

objectl = factory(Spam)
object2 = factory(Person, "Arthur", "King")
object3 = factory(Person, name='Brian')
objectl.doit(99)
print(object2.name, object2.job)
print(object3.name, object3.job)

# Listinherited p. 199

# p. 202

# p. 210

# p. 227

# p. 239 __mro__ = DFLR - duplicates

# p. 242 sample

# p. 256 slots timeit sample

# p. 262  staticmethod/classmethod


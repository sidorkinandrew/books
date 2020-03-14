# ============================== Classes

- The __init__() method is called after the instance is created. If you want to control the actual creation process, use the __new__() method.
- By convention, the __repr__() method should return a string that is a valid Python expression.
- The __str__() method is also called when you print(x).
- New in Python 3, x.__bytes__() - since the bytes type was introduced.
- By convention, format_spec should conform to the Format Specification Mini-Language. decimal.py in the Python standard library provides its own __format__() method.

# ============================== Classes That Act Like Iterators#

- The __iter__() method is called whenever you create a new iterator. It’s a good place to initialize the iterator with initial values.
- The __next__() method is called whenever you retrieve the next value from an iterator.
- The __reversed__() method is uncommon. It takes an existing sequence and returns an iterator that yields the items in the sequence in reverse order, from last to first.

# ============================== Computed Attributes#
- If your class defines a __getattribute__() method, Python will call it on every reference to any attribute or method name (except special method names, since that would cause an unpleasant infinite loop).
- If your class defines a __getattr__() method, Python will call it only after looking for the attribute in all the normal places. If an instance x defines an attribute color, x.color will not call x.__getattr__('color'); it will simply return the already-defined value of x.color.
- The __setattr__() method is called whenever you assign a value to an attribute.
- The __delattr__() method is called whenever you delete an attribute.
- The __dir__() method is useful if you define a __getattr__() or __getattribute__() method. Normally, calling dir(x) would only list the regular attributes and methods. If your __getattr__() method handles a color attribute dynamically, dir(x) would not list color as one of the available attributes. Overriding the __dir__() method allows you to list color as an available attribute, which is helpful for other people who wish to use your class without digging into the internals of it.


all attribute and method lookups go through the __getattribute__() method

# ============================== Classes That Act Like Functions#
- my_instance.__call__()

# ============================== Classes That Act Like Sets#
- the number of items	-len(s)	- s.__len__()
- to know whether it contains a specific value	- x in s	- s.__contains__(x)

# ============================== Classes That Act Like Dictionaries#
- to get a value by its key	x[key]	x.__getitem__(key)
- to set a value by its key	x[key] = value	x.__setitem__(key, value)
- to delete a key-value pair	del x[key]	x.__delitem__(key)
- to provide a default value for missing keys	x[nonexistent_key]	x.__missing__(nonexistent_key)


# ============================== Classes That Act Like Numbers#
- addition	x + y	x.__add__(y)
- subtraction	x - y	x.__sub__(y)
- multiplication	x * y	x.__mul__(y)
- division	x / y	x.__truediv__(y)
- floor division	x // y	x.__floordiv__(y)
- modulo (remainder)	x % y	x.__mod__(y)
- floor division & modulo	divmod(x, y)	x.__divmod__(y)
- raise to power	x ** y	x.__pow__(y)
- left bit-shift	x << y	x.__lshift__(y)
- right bit-shift	x >> y	x.__rshift__(y)
- bitwise and	x & y	x.__and__(y)
- bitwise xor	x ^ y	x.__xor__(y)
- bitwise or	x | y	x.__or__(y)
-- in-place
- in-place addition	x += y	x.__iadd__(y)
- in-place subtraction	x -= y	x.__isub__(y)
- in-place multiplication	x *= y	x.__imul__(y)
- in-place division	x /= y	x.__itruediv__(y)
- in-place floor division	x //= y	x.__ifloordiv__(y)
- in-place modulo	x %= y	x.__imod__(y)
- in-place raise to power	x **= y	x.__ipow__(y)
- in-place left bit-shift	x <<= y	x.__ilshift__(y)
- in-place right bit-shift	x >>= y	x.__irshift__(y)
- in-place bitwise and	x &= y	x.__iand__(y)
- in-place bitwise xor	x ^= y	x.__ixor__(y)
- in-place bitwise or	x |= y	x.__ior__(y)
-- Unary
- negative number	-x	x.__neg__()
- positive number	+x	x.__pos__()
- absolute value	abs(x)	x.__abs__()
- inverse	~x	x.__invert__()
- complex number	complex(x)	x.__complex__()
- integer	int(x)	x.__int__()
- floating point number	float(x)	x.__float__()
- number rounded to nearest integer	round(x)	x.__round__()
- number rounded to nearest n digits	round(x, n)	x.__round__(n)
- smallest integer >= x	math.ceil(x)	x.__ceil__()
- largest integer <= x	math.floor(x)	x.__floor__()
- truncate x to nearest integer toward 0	math.trunc(x)	x__trunc__()
- PEP 357	number as a list index	a_list[x]	a_list[x.__index__()]

# ============================== Classes That Can Be Compared#
- equality	x == y	x.__eq__(y)
- inequality	x != y	x.__ne__(y)
- less than	x < y	x.__lt__(y)
- less than or equal to	x <= y	x.__le__(y)
- greater than	x > y	x.__gt__(y)
- greater than or equal to	x >= y	x.__ge__(y)
- truth value in a boolean context	if x:	x.__bool__()
# If you define a __lt__() method but no __gt__() method, Python will use the __lt__() method with operands swapped. However, Python will not combine methods. For example, if you define a __lt__() method and a __eq__() method and try to test whether x <= y, Python will not call __lt__() and __eq__() in sequence. It will only call the __le__() method.

# ==============================   Classes That Can Be Serialized#
- a custom object copy	copy.copy(x)	x.__copy__()
- a custom object deepcopy	copy.deepcopy(x)	x.__deepcopy__()
*	to get an object’s state before pickling	pickle.dump(x, file)	x.__getstate__()
*	to serialize an object	pickle.dump(x, file)	x.__reduce__()
*	to serialize an object (new pickling protocol)	pickle.dump(x, file, protocol_version)	x.__reduce_ex__(protocol_version)
*	control over how an object is created during unpickling	x = pickle.load(file)	x.__getnewargs__()
*	to restore an object’s state after unpickling	x = pickle.load(file)	x.__setstate__()
# * To recreate a serialized object, Python needs to create a new object that looks like the serialized object, then set the values of all the attributes on the new object. The __getnewargs__() method controls how the object is created, then the __setstate__() method controls how the attribute values are restored.

# ==============================   Classes That Can Be Used in a with Block#
- do something special when entering a with block	with x:	x.__enter__()
- do something special when leaving a with block	with x:	x.__exit__(exc_type, exc_value, traceback)

# ==============================   Really Esoteric Stuff#
-  a class constructor	x = MyClass()	x.__new__()
*	a class destructor	del x	x.__del__()
only a specific set of attributes to be defined		x.__slots__()
a custom hash value	hash(x)	x.__hash__()
to get a property’s value	x.color	type(x).__dict__['color'].__get__(x, type(x))
to set a property’s value	x.color = 'PapayaWhip'	type(x).__dict__['color'].__set__(x, 'PapayaWhip')
to delete a property	del x.color	type(x).__dict__['color'].__del__(x)
to control whether an object is an instance of your class	isinstance(x, MyClass)	MyClass.__instancecheck__(x)
to control whether a class is a subclass of your class	issubclass(C, MyClass)	MyClass.__subclasscheck__(C)
to control whether a class is a subclass of your abstract base class	issubclass(C, MyABC)	MyABC.__subclasshook__(C)
* Exactly when Python calls the __del__() special method is incredibly complicated. To fully understand it, you need to know how Python keeps track of objects in memory. Here’s a good article on Python garbage collection and class destructors. You should also read about weak references, the weakref module, and probably the gc module for good measure.

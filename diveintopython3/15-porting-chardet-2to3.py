# https://diveintopython3.net/table-of-contents.html#case-study-porting-chardet-to-python-3
Case Study: Porting chardet to Python 3
Diving In
What is Character Encoding Auto-Detection?
Isn’t That Impossible?
Does Such An Algorithm Exist?
Introducing The chardet Module
utf-n With A bom
Escaped Encodings
Multi-Byte Encodings
Single-Byte Encodings
windows-1252
Running 2to3
A Short Digression Into Multi-File Modules
Fixing What 2to3 Can’t
False is invalid syntax
No module named constants
Name 'file' is not defined
Can’t use a string pattern on a bytes-like object
Can't convert 'bytes' object to str implicitly
Unsupported operand type(s) for +: 'int' and 'bytes'
ord() expected string of length 1, but int found
Unorderable types: int() >= str()
Global name 'reduce' is not defined
Summary

# Since json is not Python-specific, there are some mismatches in its coverage of Python datatypes. Some of them are simply naming differences, but there is two important Python datatypes that are completely missing. See if you can spot them:

JSON	Python 3
object	dictionary
array	list
string	string
integer	integer
real number	float
*	true	True
*	false	False
*	null	None

* All json values are case-sensitive.



import time

def to_json(python_object):
    if isinstance(python_object, time.struct_time):          
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(python_object)}    
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')
    
>>> with open('entry.json', 'w', encoding='utf-8') as f:
...     json.dump(entry, f, default=customserializer.to_json)

# add this to customserializer.py
def from_json(json_object):                                   
    if '__class__' in json_object:                            
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])    
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])            
    return json_object

>>> import customserializer
>>> with open('entry.json', 'r', encoding='utf-8') as f:
...  entry = json.load(f, object_hook=customserializer.from_json)


#  the value of the 'tags' key is a list of three strings. json doesn’t distinguish between tuples and lists; it only has a single list-like datatype, the array, and the json module silently converts both tuples and lists into json arrays during serialization. For most uses, you can ignore the difference between tuples and lists, but it’s something to keep in mind as you work with the json module.

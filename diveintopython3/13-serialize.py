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

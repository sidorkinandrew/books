# The __init__() method is called immediately after an instance of the class is created.
# It would be tempting — but technically incorrect — to call this the “constructor” of the class.
# It’s tempting, because it looks like a C++ constructor (by convention, the __init__() method is the first method defined for the class),
# acts like one (it’s the first piece of code executed in a newly created instance of the class), and even sounds like one.
# Incorrect, because the object has already been constructed by the time the __init__() method is called,
# and you already have a valid reference to the new instance of the class.
